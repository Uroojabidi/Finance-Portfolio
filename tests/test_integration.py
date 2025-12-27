import unittest
import pandas as pd
import tempfile
import os
import sys

# Add the project root to the Python path so we can import risk_analyzer
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from risk_analyzer import load_and_validate_data, perform_analysis


class TestWithRealData(unittest.TestCase):
    """Integration tests using real data files."""
    
    def setUp(self):
        """Set up paths to real data files."""
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        # Only use the CSV file that matches the current schema
        self.csv_files = [os.path.join(self.data_dir, 'Qwen_csv_20251225_upsmabt6b.csv')]

        # Verify the file exists
        for csv_file in self.csv_files:
            if not os.path.exists(csv_file):
                raise FileNotFoundError(f"Expected CSV file does not exist: {csv_file}")
    
    def test_load_real_csv_files(self):
        """Test loading all real CSV files in the data directory."""
        for csv_file in self.csv_files:
            with self.subTest(csv_file=csv_file):
                # Test that the file can be loaded without errors
                df = load_and_validate_data(csv_file)
                
                # Verify it has the expected columns
                expected_columns = [
                    'Loan_ID', 'Age', 'Citizenship', 'Major', 'Degree_Level', 
                    'Expected_Income', 'Employment_Status', 'Credit_Score', 
                    'Loan_Amount', 'Interest_Rate', 'Monthly_Payment', 'DTI_Ratio', 
                    'Has_Cosigner', 'Default'
                ]
                
                for col in expected_columns:
                    self.assertIn(col, df.columns)
                
                # Verify there's at least one row
                self.assertGreater(len(df), 0)
                
                print(f"Successfully loaded {csv_file}: {len(df)} rows")
    
    def test_perform_analysis_on_real_data(self):
        """Test performing analysis on real data files."""
        for csv_file in self.csv_files:
            with self.subTest(csv_file=csv_file):
                # Load the data
                df = load_and_validate_data(csv_file)
                
                # Perform analysis
                results = perform_analysis(df)
                
                # Verify results structure
                self.assertIn('summary_stats', results)
                self.assertIn('individual_assessments', results)
                self.assertIn('risk_by_major', results)
                self.assertIn('risk_by_employment', results)
                self.assertIn('risk_by_citizenship', results)
                self.assertIn('risk_by_degree', results)
                self.assertIn('recommendations', results)
                
                # Verify summary stats
                summary = results['summary_stats']
                self.assertEqual(summary['Total_Loans'], len(df))
                self.assertGreaterEqual(summary['Default_Rate'], 0)
                self.assertLessEqual(summary['Default_Rate'], 100)
                
                # Verify individual assessments
                individual = results['individual_assessments']
                self.assertEqual(len(individual), len(df))
                self.assertIn('Risk_Score', individual.columns)
                self.assertIn('Risk_Category', individual.columns)
                
                print(f"Successfully analyzed {csv_file}: {len(df)} loans, {summary['Default_Rate']:.2f}% default rate")
    
    def test_risk_distribution_in_real_data(self):
        """Test risk distribution in real data."""
        for csv_file in self.csv_files:
            with self.subTest(csv_file=csv_file):
                df = load_and_validate_data(csv_file)
                results = perform_analysis(df)
                
                individual = results['individual_assessments']
                
                # Count risk categories
                low_risk = len(individual[individual['Risk_Category'] == 'Low'])
                medium_risk = len(individual[individual['Risk_Category'] == 'Medium'])
                high_risk = len(individual[individual['Risk_Category'] == 'High'])
                
                total = len(individual)
                
                # Verify all loans are categorized
                self.assertEqual(low_risk + medium_risk + high_risk, total)
                
                print(f"Risk distribution in {os.path.basename(csv_file)}: "
                      f"Low: {low_risk}, Medium: {medium_risk}, High: {high_risk}")


if __name__ == '__main__':
    # Print information about the data files being tested
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    print(f"Testing with CSV files from: {data_dir}")
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            file_path = os.path.join(data_dir, file)
            df = pd.read_csv(file_path)
            print(f"  {file}: {len(df)} rows")
    
    unittest.main()