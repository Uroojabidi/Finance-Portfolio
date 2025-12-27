# 🧪 Test-Driven Development (TDD) Document
**Project Title**: Student Loan Default Risk Analysis – University of Chicago  
**Author**: Urooj Abidi  
**Date**: December 26, 2025  
**Tool**: LibreOffice Calc (v7.6+)  
**License**: MIT (open-source portfolio project)

---

## 1. 🎯 Objective

To implement a test-driven approach for the Student Loan Default Risk Analysis project, ensuring that all analysis functions, formulas, and outputs meet the specified requirements before implementation. This TDD document will guide the creation and validation of spreadsheet functions, data processing steps, and analysis outputs.

---

## 2. 🧪 Test Cases for Input Data Validation

### Test Case 1: Dataset Size Validation
- **Given**: A CSV file `uchicago_loan_sample.csv`
- **When**: Loading the data into LibreOffice Calc
- **Then**: The dataset should contain exactly 50 rows of data (excluding header)

### Test Case 2: Field Type Validation
- **Given**: Each column in the dataset
- **When**: Validating data types
- **Then**: Each field should match the specified type:
  - `Loan_ID`, `Student_ID`, `Gender`, `Race_Ethnicity`, `Major`, `Employment_Status`, `Loan_Type`, `Repayment_Plan` should be Text
  - `Age` should be Integer
  - `Graduated`, `Disability`, `Military`, `Default` should be Boolean
  - `Expected_Annual_Income`, `Principal_Balance`, `Monthly_Payment` should be Currency
  - `Interest_Rate` should be Percentage

### Test Case 3: Data Range Validation
- **Given**: Values in each field
- **When**: Checking value ranges
- **Then**: Values should be within reasonable ranges:
  - `Age` should be between 18-65
  - `Expected_Annual_Income` should be positive
  - `Principal_Balance` should be positive
  - `Interest_Rate` should be between 0-20%
  - `Default` should only contain "Yes" or "No"

---

## 3. 🧪 Test Cases for Calculated Fields

### Test Case 4: Payment_to_Income_Ratio Calculation
- **Given**: `Monthly_Payment` and `Expected_Annual_Income` values
- **When**: Applying the formula `=Monthly_Payment / (Expected_Annual_Income / 12)`
- **Then**: The result should be a decimal value representing the ratio

### Test Case 5: Risk_Score Calculation
- **Given**: `Graduated`, `Loan_Type`, and `Expected_Annual_Income` values
- **When**: Applying the formula `=IF(Graduated="No",2,0) + IF(Loan_Type="Private",3,0) + IF(Expected_Annual_Income<45000,2,0)`
- **Then**: The result should be an integer between 0 and 7

### Test Case 6: Risk_Category Calculation
- **Given**: `Risk_Score` value
- **When**: Applying the formula `=IF(Risk_Score>=5,"High",IF(Risk_Score>=2,"Medium","Low"))`
- **Then**: The result should be "High", "Medium", or "Low"

---

## 4. 🧪 Test Cases for PivotTables

### Test Case 7: Default Rate by Graduated PivotTable
- **Given**: Raw dataset with `Graduated` and `Default` fields
- **When**: Creating PivotTable
- **Then**: Should show default rates for "Yes" and "No" graduation status

### Test Case 8: Default Rate by Major PivotTable
- **Given**: Raw dataset with `Major` and `Default` fields
- **When**: Creating PivotTable
- **Then**: Should show default rates by major field

### Test Case 9: Average Income by Default PivotTable
- **Given**: Raw dataset with `Expected_Annual_Income` and `Default` fields
- **When**: Creating PivotTable
- **Then**: Should show average income for defaulted vs non-defaulted loans

### Test Case 10: Default Rate by Loan Type PivotTable
- **Given**: Raw dataset with `Loan_Type` and `Default` fields
- **When**: Creating PivotTable
- **Then**: Should show default rates for Federal vs Private loans

---

## 5. 🧪 Test Cases for Charts

### Test Case 11: Default % by Major Bar Chart
- **Given**: Data from Major vs Default PivotTable
- **When**: Creating bar chart
- **Then**: Should visualize default percentages by major with clear labels

### Test Case 12: Income vs Monthly Payment Scatter Plot
- **Given**: `Expected_Annual_Income` and `Monthly_Payment` data
- **When**: Creating scatter plot
- **Then**: Should color points by Default status with appropriate axes

### Test Case 13: Loan Type Distribution Pie Chart
- **Given**: Loan type distribution data
- **When**: Creating pie chart
- **Then**: Should show proportion of Federal vs Private loans

---

## 6. 🧪 Test Cases for Summary Report

### Test Case 14: Executive Summary Accuracy
- **Given**: Analysis results
- **When**: Creating executive summary
- **Then**: Should accurately reflect the findings from the analysis

### Test Case 15: Key Metrics Table
- **Given**: Calculated metrics from analysis
- **When**: Creating metrics table
- **Then**: Should include:
  - Total Loans: 50
  - Default Rate: 18%
  - Avg. Income (Default): $36,200
  - Avg. Income (Paid): $82,500
  - Default Rate (Not Graduated): 67%

### Test Case 16: Recommendations Validity
- **Given**: Analysis results
- **When**: Creating recommendations
- **Then**: Should be based on actual findings and actionable

---

## 7. 🧪 Test Cases for Output File

### Test Case 17: File Format Validation
- **Given**: `uchicago_risk_analysis.ods` file
- **When**: Opening the file in LibreOffice Calc
- **Then**: File should open without errors and contain all required sheets

### Test Case 18: Sheet Structure Validation
- **Given**: `uchicago_risk_analysis.ods` file
- **When**: Checking sheet structure
- **Then**: Should contain these sheets:
  - `Raw_Data`
  - `PivotTables`
  - `Charts`
  - `Summary_Report`

### Test Case 19: Formula Validation
- **Given**: Calculated fields in the spreadsheet
- **When**: Reviewing formulas
- **Then**: All formulas should be documented in comments or a `Formulas` sheet

---

## 8. 🧪 Test Cases for GitHub Repository

### Test Case 20: Repository Structure Validation
- **Given**: GitHub repository
- **When**: Checking repository structure
- **Then**: Should match the specified structure with all required files and directories

### Test Case 21: README Content Validation
- **Given**: README.md file
- **When**: Reviewing content
- **Then**: Should include:
  - 2–3 screenshots of key charts/tables
  - Link to public data sources
  - Note about synthetic educational project

---

## 9. ✅ TDD Implementation Steps

### Phase 1: Data Preparation
1. Write tests for data validation
2. Create synthetic dataset that passes all validation tests
3. Import data into LibreOffice Calc
4. Verify all tests pass

### Phase 2: Formula Implementation
1. Write tests for calculated fields
2. Implement formulas in spreadsheet
3. Verify all calculation tests pass

### Phase 3: Analysis Implementation
1. Write tests for PivotTables and charts
2. Create PivotTables and charts
3. Verify all visualization tests pass

### Phase 4: Report Generation
1. Write tests for summary report
2. Create summary report
3. Verify all report tests pass

### Phase 5: Integration Testing
1. Write tests for complete workflow
2. Validate entire analysis process
3. Verify all integration tests pass

---

## 10. 📋 TDD Success Criteria

The TDD approach is successful when:
- [ ] All 21 test cases pass
- [ ] Each feature is developed with tests written first
- [ ] All formulas and calculations are validated
- [ ] Analysis results are accurate and reproducible
- [ ] Final output meets PRD requirements