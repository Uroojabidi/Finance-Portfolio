import unittest
import pandas as pd
import tempfile
import os
from unittest.mock import patch, MagicMock
import sys
import argparse

# Add the project root to the Python path so we can import risk_analyzer
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from risk_analyzer import (
    calculate_risk_score, 
    assign_risk_category, 
    calculate_payment_to_income_ratio,
    load_and_validate_data,
    perform_analysis,
    generate_output,
    main
)


class TestRiskCalculations(unittest.TestCase):
    """Test risk calculation functions."""
    
    def setUp(self):
        """Set up test data."""
        self.test_row = pd.Series({
            'Employment_Status': 'Employed',
            'Expected_Income': 50000,
            'DTI_Ratio': 0.15,
            'Credit_Score': 700,
            'Citizenship': 'U.S.',
            'Degree_Level': 'Bachelor',
            'Monthly_Payment': 500
        })
    
    def test_calculate_risk_score_employed_low_income(self):
        """Test risk score calculation for employed person with low income."""
        row = self.test_row.copy()
        row['Expected_Income'] = 40000  # Below $45,000 threshold
        score = calculate_risk_score(row)
        # Employed (0) + Low income (2) + DTI <= 0.20 (0) + Good credit (0) + US (0) + Bachelor (1) = 3
        self.assertEqual(score, 3)
    
    def test_calculate_risk_score_unemployed(self):
        """Test risk score calculation for unemployed person."""
        row = self.test_row.copy()
        row['Employment_Status'] = 'Unemployed'
        score = calculate_risk_score(row)
        # Unemployed (3) + Income >= 45k (0) + DTI <= 0.20 (0) + Good credit (0) + US (0) + Bachelor (1) = 4
        self.assertEqual(score, 4)
    
    def test_calculate_risk_score_high_dti(self):
        """Test risk score calculation for high DTI ratio."""
        row = self.test_row.copy()
        row['DTI_Ratio'] = 0.25  # Above 0.20 threshold
        score = calculate_risk_score(row)
        # Employed (0) + Income >= 45k (0) + High DTI (2) + Good credit (0) + US (0) + Bachelor (1) = 3
        self.assertEqual(score, 3)
    
    def test_calculate_risk_score_low_credit(self):
        """Test risk score calculation for low credit score."""
        row = self.test_row.copy()
        row['Credit_Score'] = 550  # Below 600 threshold
        score = calculate_risk_score(row)
        # Employed (0) + Income >= 45k (0) + DTI <= 0.20 (0) + Low credit (1) + US (0) + Bachelor (1) = 2
        self.assertEqual(score, 2)
    
    def test_calculate_risk_score_international(self):
        """Test risk score calculation for international student."""
        row = self.test_row.copy()
        row['Citizenship'] = 'International'
        score = calculate_risk_score(row)
        # Employed (0) + Income >= 45k (0) + DTI <= 0.20 (0) + Good credit (0) + International (1) + Bachelor (1) = 2
        self.assertEqual(score, 2)
    
    def test_calculate_risk_score_all_factors(self):
        """Test risk score calculation with all risk factors."""
        row = pd.Series({
            'Employment_Status': 'Unemployed',
            'Expected_Income': 40000,
            'DTI_Ratio': 0.25,
            'Credit_Score': 550,
            'Citizenship': 'International',
            'Degree_Level': 'Bachelor'
        })
        score = calculate_risk_score(row)
        # Unemployed (3) + Low income (2) + High DTI (2) + Low credit (1) + International (1) + Bachelor (1) = 10
        self.assertEqual(score, 10)
    
    def test_assign_risk_category_low(self):
        """Test risk category assignment for low risk."""
        self.assertEqual(assign_risk_category(0), 'Low')
        self.assertEqual(assign_risk_category(1), 'Low')
    
    def test_assign_risk_category_medium(self):
        """Test risk category assignment for medium risk."""
        self.assertEqual(assign_risk_category(2), 'Medium')
        self.assertEqual(assign_risk_category(3), 'Medium')
        self.assertEqual(assign_risk_category(4), 'Medium')
    
    def test_assign_risk_category_high(self):
        """Test risk category assignment for high risk."""
        self.assertEqual(assign_risk_category(5), 'High')
        self.assertEqual(assign_risk_category(6), 'High')
    
    def test_calculate_payment_to_income_ratio(self):
        """Test payment-to-income ratio calculation."""
        row = pd.Series({
            'Monthly_Payment': 500,
            'Expected_Income': 60000
        })
        ratio = calculate_payment_to_income_ratio(row)
        # 500 / (60000 / 12) = 500 / 5000 = 0.1
        self.assertEqual(ratio, 0.1)
    
    def test_calculate_payment_to_income_ratio_zero_income(self):
        """Test payment-to-income ratio calculation with zero income."""
        row = pd.Series({
            'Monthly_Payment': 500,
            'Expected_Income': 0
        })
        ratio = calculate_payment_to_income_ratio(row)
        self.assertEqual(ratio, 0.0)


class TestDataLoading(unittest.TestCase):
    """Test data loading and validation functions."""
    
    def setUp(self):
        """Set up test CSV data."""
        self.test_csv_content = """Loan_ID,Age,Citizenship,Major,Degree_Level,Expected_Income,Employment_Status,Credit_Score,Loan_Amount,Interest_Rate,Monthly_Payment,DTI_Ratio,Has_Cosigner,Default
TEST001,22,U.S.,Economics,Bachelor,65000,Employed,720,30000,6.2,335,0.062,Yes,No
TEST002,24,International,Physics,PhD,95000,Employed,N/A,50000,8.5,580,0.073,No,No
TEST003,23,U.S.,English,Bachelor,38000,Unemployed,610,42000,9.1,480,0.152,No,Yes"""
    
    def test_load_and_validate_data_success(self):
        """Test successful loading and validation of data."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(self.test_csv_content)
            temp_file = f.name
        
        try:
            df = load_and_validate_data(temp_file)
            self.assertEqual(len(df), 3)
            self.assertEqual(df['Loan_ID'].iloc[0], 'TEST001')
            self.assertEqual(df['Default'].iloc[2], 'Yes')
        finally:
            os.unlink(temp_file)
    
    def test_load_and_validate_data_missing_file(self):
        """Test error handling for missing file."""
        with self.assertRaises(FileNotFoundError):
            load_and_validate_data('nonexistent.csv')
    
    def test_load_and_validate_data_missing_columns(self):
        """Test error handling for missing required columns."""
        csv_content = """Loan_ID,Age,Citizenship,Major,Degree_Level,Expected_Income,Employment_Status,Credit_Score,Loan_Amount,Interest_Rate,Monthly_Payment,DTI_Ratio,Has_Cosigner
TEST001,22,U.S.,Economics,Bachelor,65000,Employed,720,30000,6.2,335,0.062,Yes"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            temp_file = f.name
        
        try:
            with self.assertRaises(ValueError):
                load_and_validate_data(temp_file)
        finally:
            os.unlink(temp_file)


class TestAnalysis(unittest.TestCase):
    """Test analysis functions."""
    
    def setUp(self):
        """Set up test data."""
        self.test_data = pd.DataFrame({
            'Loan_ID': ['TEST001', 'TEST002', 'TEST003'],
            'Age': [22, 24, 23],
            'Citizenship': ['U.S.', 'International', 'U.S.'],
            'Major': ['Economics', 'Physics', 'English'],
            'Degree_Level': ['Bachelor', 'PhD', 'Bachelor'],
            'Expected_Income': [65000, 95000, 38000],
            'Employment_Status': ['Employed', 'Employed', 'Unemployed'],
            'Credit_Score': [720, 'N/A', 610],
            'Loan_Amount': [30000, 50000, 42000],
            'Interest_Rate': [6.2, 8.5, 9.1],
            'Monthly_Payment': [335, 580, 480],
            'DTI_Ratio': [0.062, 0.073, 0.152],
            'Has_Cosigner': ['Yes', 'No', 'No'],
            'Default': ['No', 'No', 'Yes']
        })
    
    def test_perform_analysis(self):
        """Test the perform_analysis function."""
        results = perform_analysis(self.test_data)
        
        # Check that results contain expected keys
        self.assertIn('summary_stats', results)
        self.assertIn('individual_assessments', results)
        self.assertIn('risk_by_major', results)
        self.assertIn('risk_by_employment', results)
        self.assertIn('risk_by_citizenship', results)
        self.assertIn('risk_by_degree', results)
        self.assertIn('recommendations', results)
        
        # Check summary statistics
        summary = results['summary_stats']
        self.assertEqual(summary['Total_Loans'], 3)
        self.assertAlmostEqual(summary['Default_Rate'], 33.33, places=2)
        
        # Check individual assessments
        individual = results['individual_assessments']
        self.assertEqual(len(individual), 3)
        self.assertIn('Risk_Score', individual.columns)
        self.assertIn('Risk_Category', individual.columns)
        
        # Check that risk scores are calculated
        test003_row = individual[individual['Loan_ID'] == 'TEST003']
        self.assertEqual(len(test003_row), 1)
        # TEST003 should have high risk: Unemployed(3) + Low income(2) + DTI <= 0.20(0) + Good credit(0) + US(0) + Bachelor(1) = 6
        self.assertEqual(test003_row.iloc[0]['Risk_Score'], 6)


class TestCLIFunctionality(unittest.TestCase):
    """Test CLI functionality."""
    
    @patch('sys.argv', ['risk_analyzer.py', '--input', 'dummy.csv', '--output', 'dummy_output.csv'])
    @patch('risk_analyzer.load_and_validate_data')
    @patch('risk_analyzer.perform_analysis')
    @patch('risk_analyzer.generate_output')
    def test_main_function_calls(self, mock_generate, mock_perform, mock_load):
        """Test that main function calls the right functions."""
        # Mock the data loading
        mock_df = pd.DataFrame({
            'Loan_ID': ['TEST001'],
            'Age': [22],
            'Citizenship': ['U.S.'],
            'Major': ['Economics'],
            'Degree_Level': ['Bachelor'],
            'Expected_Income': [65000],
            'Employment_Status': ['Employed'],
            'Credit_Score': [720],
            'Loan_Amount': [30000],
            'Interest_Rate': [6.2],
            'Monthly_Payment': [335],
            'DTI_Ratio': [0.062],
            'Has_Cosigner': ['Yes'],
            'Default': ['No']
        })
        mock_load.return_value = mock_df
        
        # Mock the analysis results
        mock_analysis_results = {
            'summary_stats': {'Total_Loans': 1, 'Default_Rate': 0.0},
            'individual_assessments': pd.DataFrame({'Loan_ID': ['TEST001'], 'Risk_Score': [1], 'Risk_Category': ['Low'], 'Default': ['No']}),
            'risk_by_major': pd.DataFrame(),
            'risk_by_employment': pd.DataFrame(),
            'risk_by_citizenship': pd.DataFrame(),
            'risk_by_degree': pd.DataFrame(),
            'recommendations': []
        }
        mock_perform.return_value = mock_analysis_results
        
        # Call main function
        main()
        
        # Verify that the functions were called
        mock_load.assert_called_once()
        mock_perform.assert_called_once()
        mock_generate.assert_called_once()


if __name__ == '__main__':
    unittest.main()