# 🧪 Test-Driven Development (TDD) Document
**Repository**: https://github.com/Uroojabidi/Finance-Portfolio/
**Project Title**: Student Loan Default Risk Analysis – University of Chicago
**Author**: Urooj Abidi
**Email**: uroojabid203@gmail.com
**Date**: December 26, 2025
**Tool**: Python CLI Application
**License**: MIT (open-source portfolio project)

---

## 1. 🎯 Objective

To implement a test-driven approach for the Student Loan Default Risk Analysis project, ensuring that all analysis functions, risk calculations, and outputs meet the specified requirements before implementation. This TDD document will guide the creation and validation of Python functions, data processing steps, and analysis outputs.

---

## 2. 🧪 Test Cases for CLI Interface

### Test Case 1: Argument Parsing Validation
- **Given**: Command line arguments with input CSV path
- **When**: Running `python risk_analyzer.py --input data.csv`
- **Then**: The application should parse the input argument correctly

### Test Case 2: Output Path Validation
- **Given**: Command line arguments with input and output paths
- **When**: Running `python risk_analyzer.py --input data.csv --output report.csv`
- **Then**: The application should use the specified output path

### Test Case 3: Help Message Validation
- **Given**: Command with help flag
- **When**: Running `python risk_analyzer.py --help`
- **Then**: The application should display usage instructions

---

## 3. 🧪 Test Cases for Input Data Validation

### Test Case 4: CSV File Loading
- **Given**: A valid CSV file with loan data
- **When**: Loading the data using pandas
- **Then**: The dataset should load without errors and contain expected columns

### Test Case 5: Required Fields Validation
- **Given**: A CSV file with loan data
- **When**: Validating required columns
- **Then**: All required fields should be present:
  - `Loan_ID`, `Age`, `Citizenship`, `Major`, `Degree_Level`, `Expected_Income`
  - `Employment_Status`, `Credit_Score`, `Loan_Amount`, `Interest_Rate`
  - `Monthly_Payment`, `DTI_Ratio`, `Has_Cosigner`, `Default`

### Test Case 6: Data Type Validation
- **Given**: Each column in the dataset
- **When**: Validating data types
- **Then**: Each field should match the specified type:
  - `Loan_ID`, `Citizenship`, `Major`, `Degree_Level`, `Employment_Status`, `Has_Cosigner`, `Default` should be Text
  - `Age`, `Expected_Income`, `Loan_Amount`, `Monthly_Payment` should be Integer
  - `Interest_Rate`, `DTI_Ratio` should be Float
  - `Credit_Score` should be Integer or N/A

### Test Case 7: Data Range Validation
- **Given**: Values in each field
- **When**: Checking value ranges
- **Then**: Values should be within reasonable ranges:
  - `Age` should be between 18-65
  - `Expected_Income` should be positive
  - `Loan_Amount` should be positive
  - `Interest_Rate` should be between 0-20%
  - `DTI_Ratio` should be non-negative
  - `Default` should only contain "Yes" or "No"

---

## 4. 🧪 Test Cases for Calculated Fields

### Test Case 8: Payment_to_Income_Ratio Calculation
- **Given**: `Monthly_Payment` and `Expected_Income` values
- **When**: Calculating `Monthly_Payment / (Expected_Income / 12)`
- **Then**: The result should be a float value representing the ratio

### Test Case 9: Risk_Score Calculation
- **Given**: Employment status, Expected_Income, DTI_Ratio, Credit_Score, Citizenship, Degree_Level
- **When**: Calculating weighted risk score
- **Then**: The result should be an integer based on risk factors:
  - Unemployed = 3 points
  - Income < $45,000 = 2 points
  - DTI_Ratio > 0.20 = 2 points
  - Credit_Score < 600 = 1 point
  - International = 1 point
  - Bachelor = 1 point

### Test Case 10: Risk_Category Calculation
- **Given**: `Risk_Score` value
- **When**: Categorizing risk based on thresholds
- **Then**: The result should be "Low", "Medium", or "High":
  - Score < 2 = "Low"
  - 2 ≤ Score ≤ 4 = "Medium"
  - Score > 4 = "High"

---

## 5. 🧪 Test Cases for Analysis Functions

### Test Case 11: Default Rate Calculation
- **Given**: Dataset with Default column
- **When**: Calculating overall default rate
- **Then**: Should return the percentage of "Yes" values in Default column

### Test Case 12: Default Rate by Major
- **Given**: Dataset grouped by Major and Default
- **When**: Calculating default rates by major
- **Then**: Should return a table with default rates for each major

### Test Case 13: Average Income by Default Status
- **Given**: Dataset with Expected_Income and Default columns
- **When**: Calculating average income by default status
- **Then**: Should return average income for "Yes" and "No" default values

### Test Case 14: Default Rate by Employment Status
- **Given**: Dataset grouped by Employment_Status and Default
- **When**: Calculating default rates by employment status
- **Then**: Should return default rates for employed vs unemployed

---

## 6. 🧪 Test Cases for Output Generation

### Test Case 15: CSV Output Format Validation
- **Given**: Risk analysis results
- **When**: Generating CSV output
- **Then**: Output should be a properly formatted CSV with all required sections

### Test Case 16: Summary Statistics Output
- **Given**: Analysis results
- **When**: Creating summary statistics section
- **Then**: Should include Total Loans, Default Rate, Avg. Income, etc.

### Test Case 17: Individual Risk Assessments Output
- **Given**: Calculated risk scores for each loan
- **When**: Creating individual assessments section
- **Then**: Should include Loan_ID, Risk_Score, Risk_Category for each loan

### Test Case 18: Risk Factor Analysis Output
- **Given**: Grouped analysis results
- **When**: Creating risk factor analysis section
- **Then**: Should include default rates by major, employment status, etc.

---

## 7. 🧪 Test Cases for Error Handling

### Test Case 19: Missing Input File
- **Given**: Non-existent CSV file path
- **When**: Attempting to load the file
- **Then**: Should display appropriate error message and exit gracefully

### Test Case 20: Invalid CSV Format
- **Given**: CSV file with incorrect format or missing columns
- **When**: Attempting to process the file
- **Then**: Should display appropriate error message and exit gracefully

### Test Case 21: Invalid Data Values
- **Given**: CSV file with invalid data (negative income, etc.)
- **When**: Processing the data
- **Then**: Should handle errors appropriately and continue processing valid records

---

## 8. ✅ TDD Implementation Steps

### Phase 1: Environment Setup
1. Write tests for CLI argument parsing
2. Implement argument parsing functionality
3. Verify all argument parsing tests pass

### Phase 2: Data Loading and Validation
1. Write tests for CSV loading and validation
2. Implement data loading and validation functions
3. Verify all data validation tests pass

### Phase 3: Risk Calculation Implementation
1. Write tests for calculated fields (Payment_to_Income_Ratio, Risk_Score, Risk_Category)
2. Implement risk calculation functions
3. Verify all calculation tests pass

### Phase 4: Analysis Functions Implementation
1. Write tests for analysis functions (default rates, averages, etc.)
2. Implement analysis functions
3. Verify all analysis tests pass

### Phase 5: Output Generation
1. Write tests for CSV output generation
2. Implement output generation functions
3. Verify all output tests pass

### Phase 6: Integration Testing
1. Write tests for complete workflow
2. Validate entire analysis process
3. Verify all integration tests pass

---

## 9. 📋 TDD Success Criteria

The TDD approach is successful when:
- [ ] All 21 test cases pass
- [ ] Each feature is developed with tests written first
- [ ] All risk calculations are validated
- [ ] Analysis results are accurate and reproducible
- [ ] Final output meets PRD requirements
- [ ] Application handles errors gracefully
- [ ] CLI interface works as expected