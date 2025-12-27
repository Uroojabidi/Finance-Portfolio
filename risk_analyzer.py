#!/usr/bin/env python3
"""
Student Loan Default Risk Analysis CLI Tool

This application analyzes student loan data to identify risk factors for default
and generates a comprehensive risk analysis report in CSV format.
"""

import argparse
import pandas as pd
import sys
import os
from typing import Dict, Any


def calculate_risk_score(row: pd.Series) -> int:
    """
    Calculate risk score based on multiple factors.
    
    Risk factors and their weights:
    - Employment Status: Unemployed = 3 points, Employed = 0 points
    - Expected Income: < $45,000 = 2 points, ≥ $45,000 = 0 points
    - DTI Ratio: > 0.20 = 2 points, ≤ 0.20 = 0 points
    - Credit Score: < 600 = 1 point, ≥ 600 or N/A = 0 points
    - Citizenship: International = 1 point, U.S. = 0 points
    - Degree Level: Bachelor = 1 point, Master = 0, PhD = 0, JD = 0
    """
    score = 0
    
    # Employment Status: Unemployed = 3 points
    if row['Employment_Status'] == 'Unemployed':
        score += 3
    
    # Expected Income: < $45,000 = 2 points
    if row['Expected_Income'] < 45000:
        score += 2
    
    # DTI Ratio: > 0.20 = 2 points
    if row['DTI_Ratio'] > 0.20:
        score += 2
    
    # Credit Score: < 600 = 1 point (N/A is treated as neutral)
    if pd.notna(row['Credit_Score']) and row['Credit_Score'] != 'N/A':
        try:
            credit_score = int(row['Credit_Score'])
            if credit_score < 600:
                score += 1
        except ValueError:
            # If credit score is not a valid integer, treat as neutral
            pass
    
    # Citizenship: International = 1 point
    if row['Citizenship'] == 'International':
        score += 1
    
    # Degree Level: Bachelor = 1 point
    if row['Degree_Level'] == 'Bachelor':
        score += 1
    
    return score


def assign_risk_category(risk_score: int) -> str:
    """Assign risk category based on risk score."""
    if risk_score < 2:
        return 'Low'
    elif risk_score <= 4:
        return 'Medium'
    else:
        return 'High'


def calculate_payment_to_income_ratio(row: pd.Series) -> float:
    """Calculate payment-to-income ratio."""
    if row['Expected_Income'] == 0:
        return 0.0  # Avoid division by zero
    return row['Monthly_Payment'] / (row['Expected_Income'] / 12)


def load_and_validate_data(input_file: str) -> pd.DataFrame:
    """Load and validate input CSV data."""
    # Check if file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file does not exist: {input_file}")
    
    # Load the CSV file
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {str(e)}")
    
    # Required columns
    required_columns = [
        'Loan_ID', 'Age', 'Citizenship', 'Major', 'Degree_Level', 
        'Expected_Income', 'Employment_Status', 'Credit_Score', 
        'Loan_Amount', 'Interest_Rate', 'Monthly_Payment', 'DTI_Ratio', 
        'Has_Cosigner', 'Default'
    ]
    
    # Check if all required columns exist
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Validate data types and ranges where possible
    # Age validation
    if not pd.api.types.is_numeric_dtype(df['Age']):
        try:
            df['Age'] = pd.to_numeric(df['Age'])
        except ValueError:
            raise ValueError("Age column must contain numeric values")
    
    age_invalid = df[(df['Age'] < 18) | (df['Age'] > 65)]
    if not age_invalid.empty:
        print(f"Warning: Found {len(age_invalid)} records with invalid age (18-65 range)", file=sys.stderr)
    
    # Income validation
    if not pd.api.types.is_numeric_dtype(df['Expected_Income']):
        try:
            df['Expected_Income'] = pd.to_numeric(df['Expected_Income'])
        except ValueError:
            raise ValueError("Expected_Income column must contain numeric values")
    
    income_invalid = df[df['Expected_Income'] <= 0]
    if not income_invalid.empty:
        raise ValueError("Expected_Income must be positive for all records")
    
    # Loan amount validation
    if not pd.api.types.is_numeric_dtype(df['Loan_Amount']):
        try:
            df['Loan_Amount'] = pd.to_numeric(df['Loan_Amount'])
        except ValueError:
            raise ValueError("Loan_Amount column must contain numeric values")
    
    loan_invalid = df[df['Loan_Amount'] <= 0]
    if not loan_invalid.empty:
        raise ValueError("Loan_Amount must be positive for all records")
    
    # Interest rate validation
    if not pd.api.types.is_numeric_dtype(df['Interest_Rate']):
        try:
            df['Interest_Rate'] = pd.to_numeric(df['Interest_Rate'])
        except ValueError:
            raise ValueError("Interest_Rate column must contain numeric values")
    
    # Monthly payment validation
    if not pd.api.types.is_numeric_dtype(df['Monthly_Payment']):
        try:
            df['Monthly_Payment'] = pd.to_numeric(df['Monthly_Payment'])
        except ValueError:
            raise ValueError("Monthly_Payment column must contain numeric values")
    
    # DTI Ratio validation
    if not pd.api.types.is_numeric_dtype(df['DTI_Ratio']):
        try:
            df['DTI_Ratio'] = pd.to_numeric(df['DTI_Ratio'])
        except ValueError:
            raise ValueError("DTI_Ratio column must contain numeric values")
    
    dti_invalid = df[df['DTI_Ratio'] < 0]
    if not dti_invalid.empty:
        raise ValueError("DTI_Ratio must be non-negative for all records")
    
    # Default validation
    invalid_defaults = df[~df['Default'].isin(['Yes', 'No'])]
    if not invalid_defaults.empty:
        raise ValueError("Default column must contain only 'Yes' or 'No' values")
    
    return df


def perform_analysis(df: pd.DataFrame) -> Dict[str, Any]:
    """Perform comprehensive risk analysis on the data."""
    results = {}
    
    # Calculate additional fields
    df = df.copy()
    df['Payment_to_Income_Ratio'] = df.apply(calculate_payment_to_income_ratio, axis=1)
    df['Risk_Score'] = df.apply(calculate_risk_score, axis=1)
    df['Risk_Category'] = df['Risk_Score'].apply(assign_risk_category)
    
    # Summary statistics
    results['summary_stats'] = {
        'Total_Loans': len(df),
        'Default_Rate': (df['Default'] == 'Yes').sum() / len(df) * 100,
        'Avg_Income_Default_Yes': df[df['Default'] == 'Yes']['Expected_Income'].mean() if (df['Default'] == 'Yes').any() else 0,
        'Avg_Income_Default_No': df[df['Default'] == 'No']['Expected_Income'].mean() if (df['Default'] == 'No').any() else 0,
        'Avg_Loan_Amount': df['Loan_Amount'].mean(),
        'Avg_Interest_Rate': df['Interest_Rate'].mean(),
        'Avg_Monthly_Payment': df['Monthly_Payment'].mean(),
        'Avg_DTI_Ratio': df['DTI_Ratio'].mean(),
    }
    
    # Risk factor analysis by major
    results['risk_by_major'] = df.groupby('Major').agg({
        'Default': lambda x: (x == 'Yes').sum() / len(x) * 100,
        'Risk_Score': 'mean',
        'Expected_Income': 'mean',
        'Loan_Amount': 'mean'
    }).round(2).reset_index()
    results['risk_by_major'].columns = ['Major', 'Default_Rate_Pct', 'Avg_Risk_Score', 'Avg_Income', 'Avg_Loan_Amount']
    
    # Risk factor analysis by employment status
    results['risk_by_employment'] = df.groupby('Employment_Status').agg({
        'Default': lambda x: (x == 'Yes').sum() / len(x) * 100,
        'Risk_Score': 'mean',
        'Expected_Income': 'mean'
    }).round(2).reset_index()
    results['risk_by_employment'].columns = ['Employment_Status', 'Default_Rate_Pct', 'Avg_Risk_Score', 'Avg_Income']
    
    # Risk factor analysis by citizenship
    results['risk_by_citizenship'] = df.groupby('Citizenship').agg({
        'Default': lambda x: (x == 'Yes').sum() / len(x) * 100,
        'Risk_Score': 'mean',
        'Expected_Income': 'mean'
    }).round(2).reset_index()
    results['risk_by_citizenship'].columns = ['Citizenship', 'Default_Rate_Pct', 'Avg_Risk_Score', 'Avg_Income']
    
    # Risk factor analysis by degree level
    results['risk_by_degree'] = df.groupby('Degree_Level').agg({
        'Default': lambda x: (x == 'Yes').sum() / len(x) * 100,
        'Risk_Score': 'mean',
        'Expected_Income': 'mean'
    }).round(2).reset_index()
    results['risk_by_degree'].columns = ['Degree_Level', 'Default_Rate_Pct', 'Avg_Risk_Score', 'Avg_Income']
    
    # Individual risk assessments
    results['individual_assessments'] = df[['Loan_ID', 'Risk_Score', 'Risk_Category', 'Default']].copy().reset_index(drop=True)
    
    # Recommendations based on analysis
    high_risk_count = (df['Risk_Category'] == 'High').sum()
    unemployed_default_rate = 0
    if 'Unemployed' in df['Employment_Status'].values:
        unemployed_default_rate = (df[df['Employment_Status'] == 'Unemployed']['Default'] == 'Yes').sum() / \
                                  len(df[df['Employment_Status'] == 'Unemployed']) * 100
    
    results['recommendations'] = [
        f"High-risk loans identified: {high_risk_count} out of {len(df)} total loans",
        f"Unemployed borrowers have a default rate of {unemployed_default_rate:.2f}%",
        f"Average default rate across all loans: {results['summary_stats']['Default_Rate']:.2f}%",
        "Consider enhanced monitoring for high-risk borrowers",
        "Focus financial counseling on unemployed and low-income borrowers"
    ]
    
    return results


def generate_output(results: Dict[str, Any], output_file: str):
    """Generate comprehensive CSV output with all analysis results."""
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a list to hold all rows for the final CSV
    all_rows = []

    # Add summary statistics
    summary_stats = results['summary_stats']
    for key, value in summary_stats.items():
        all_rows.append({
            'Analysis_Section': 'Summary_Statistics',
            'Metric': key,
            'Value': value,
            'Loan_ID': '',
            'Risk_Score': '',
            'Risk_Category': '',
            'Default_Status': '',
            'Major': '',
            'Default_Rate_Pct': '',
            'Avg_Risk_Score': '',
            'Avg_Income': '',
            'Avg_Loan_Amount': '',
            'Employment_Status': '',
            'Citizenship': '',
            'Degree_Level': '',
            'Recommendation_Number': '',
            'Recommendation_Text': ''
        })

    # Add individual assessments
    individual_df = results['individual_assessments']
    for _, row in individual_df.iterrows():
        all_rows.append({
            'Analysis_Section': 'Individual_Assessments',
            'Metric': '',
            'Value': '',
            'Loan_ID': row['Loan_ID'],
            'Risk_Score': row['Risk_Score'],
            'Risk_Category': row['Risk_Category'],
            'Default_Status': row['Default'],
            'Major': '',
            'Default_Rate_Pct': '',
            'Avg_Risk_Score': '',
            'Avg_Income': '',
            'Avg_Loan_Amount': '',
            'Employment_Status': '',
            'Citizenship': '',
            'Degree_Level': '',
            'Recommendation_Number': '',
            'Recommendation_Text': ''
        })

    # Add risk by major
    major_df = results['risk_by_major']
    for _, row in major_df.iterrows():
        all_rows.append({
            'Analysis_Section': 'Risk_By_Major',
            'Metric': '',
            'Value': '',
            'Loan_ID': '',
            'Risk_Score': '',
            'Risk_Category': '',
            'Default_Status': '',
            'Major': row['Major'],
            'Default_Rate_Pct': row['Default_Rate_Pct'],
            'Avg_Risk_Score': row['Avg_Risk_Score'],
            'Avg_Income': row['Avg_Income'],
            'Avg_Loan_Amount': row['Avg_Loan_Amount'],
            'Employment_Status': '',
            'Citizenship': '',
            'Degree_Level': '',
            'Recommendation_Number': '',
            'Recommendation_Text': ''
        })

    # Add risk by employment
    employment_df = results['risk_by_employment']
    for _, row in employment_df.iterrows():
        all_rows.append({
            'Analysis_Section': 'Risk_By_Employment',
            'Metric': '',
            'Value': '',
            'Loan_ID': '',
            'Risk_Score': '',
            'Risk_Category': '',
            'Default_Status': '',
            'Major': '',
            'Default_Rate_Pct': row['Default_Rate_Pct'],
            'Avg_Risk_Score': row['Avg_Risk_Score'],
            'Avg_Income': row['Avg_Income'],
            'Employment_Status': row['Employment_Status'],
            'Citizenship': '',
            'Degree_Level': '',
            'Recommendation_Number': '',
            'Recommendation_Text': ''
        })

    # Add risk by citizenship
    citizenship_df = results['risk_by_citizenship']
    for _, row in citizenship_df.iterrows():
        all_rows.append({
            'Analysis_Section': 'Risk_By_Citizenship',
            'Metric': '',
            'Value': '',
            'Loan_ID': '',
            'Risk_Score': '',
            'Risk_Category': '',
            'Default_Status': '',
            'Major': '',
            'Default_Rate_Pct': row['Default_Rate_Pct'],
            'Avg_Risk_Score': row['Avg_Risk_Score'],
            'Avg_Income': row['Avg_Income'],
            'Employment_Status': '',
            'Citizenship': row['Citizenship'],
            'Degree_Level': '',
            'Recommendation_Number': '',
            'Recommendation_Text': ''
        })

    # Add risk by degree
    degree_df = results['risk_by_degree']
    for _, row in degree_df.iterrows():
        all_rows.append({
            'Analysis_Section': 'Risk_By_Degree',
            'Metric': '',
            'Value': '',
            'Loan_ID': '',
            'Risk_Score': '',
            'Risk_Category': '',
            'Default_Status': '',
            'Major': '',
            'Default_Rate_Pct': row['Default_Rate_Pct'],
            'Avg_Risk_Score': row['Avg_Risk_Score'],
            'Avg_Income': row['Avg_Income'],
            'Employment_Status': '',
            'Citizenship': '',
            'Degree_Level': row['Degree_Level'],
            'Recommendation_Number': '',
            'Recommendation_Text': ''
        })

    # Add recommendations
    recommendations_list = results['recommendations']
    for i, rec in enumerate(recommendations_list):
        all_rows.append({
            'Analysis_Section': 'Recommendations',
            'Metric': '',
            'Value': '',
            'Loan_ID': '',
            'Risk_Score': '',
            'Risk_Category': '',
            'Default_Status': '',
            'Major': '',
            'Default_Rate_Pct': '',
            'Avg_Risk_Score': '',
            'Avg_Income': '',
            'Employment_Status': '',
            'Citizenship': '',
            'Degree_Level': '',
            'Recommendation_Number': i+1,
            'Recommendation_Text': rec
        })

    # Create the final dataframe and save to CSV
    all_data = pd.DataFrame(all_rows)
    all_data.to_csv(output_file, index=False)

    print(f"Risk analysis report generated successfully: {output_file}")
    print(f"Total records in report: {len(all_data)}")
    print(f"Summary - Total Loans: {results['summary_stats']['Total_Loans']}, "
          f"Default Rate: {results['summary_stats']['Default_Rate']:.2f}%")


def main():
    """Main function to run the CLI application."""
    parser = argparse.ArgumentParser(
        description="Student Loan Default Risk Analysis Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python risk_analyzer.py --input data.csv --output report.csv
  python risk_analyzer.py --input data.csv  # Uses default output name
        """
    )
    
    parser.add_argument(
        '--input',
        required=True,
        help='Path to input CSV file containing loan data'
    )
    
    parser.add_argument(
        '--output',
        default='risk_report.csv',
        help='Path for output CSV report (default: risk_report.csv)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Input file: {args.input}")
        print(f"Output file: {args.output}")
    
    try:
        # Load and validate data
        if args.verbose:
            print("Loading and validating data...")
        df = load_and_validate_data(args.input)
        print(f"Loaded {len(df)} loan records from {args.input}")
        
        # Perform analysis
        if args.verbose:
            print("Performing risk analysis...")
        results = perform_analysis(df)
        
        # Generate output
        if args.verbose:
            print("Generating output report...")
        generate_output(results, args.output)
        
        # Print summary to console
        print("\n--- Analysis Summary ---")
        summary = results['summary_stats']
        print(f"Total Loans Analyzed: {summary['Total_Loans']}")
        print(f"Overall Default Rate: {summary['Default_Rate']:.2f}%")

        # Safely print average income values, handling cases where no defaults exist
        avg_income_default = summary.get('Avg_Income_Default_Yes', 0)
        avg_income_no_default = summary.get('Avg_Income_Default_No', 0)
        print(f"Average Income (Default): ${avg_income_default:,.2f}")
        print(f"Average Income (No Default): ${avg_income_no_default:,.2f}")

        # Get risk category counts from individual assessments
        individual_df = results['individual_assessments']
        high_risk_count = (individual_df['Risk_Category'] == 'High').sum()
        medium_risk_count = (individual_df['Risk_Category'] == 'Medium').sum()
        low_risk_count = (individual_df['Risk_Category'] == 'Low').sum()

        print(f"High Risk Loans: {high_risk_count}")
        print(f"Medium Risk Loans: {medium_risk_count}")
        print(f"Low Risk Loans: {low_risk_count}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Data validation error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()