# 🧪 Data Validation Tests

**Project Title**: Student Loan Default Risk Analysis – University of Chicago  
**Author**: Urooj Abidi  
**Date**: December 26, 2025  
**Tool**: LibreOffice Calc (v7.6+)  
**License**: MIT (open-source portfolio project)

---

## 1. 🎯 Test Overview

This document outlines the validation tests for the student loan dataset to ensure data quality, completeness, and adherence to the specified schema requirements.

---

## 2. 📋 Test Cases

### Test Case 1: Dataset Size Validation
- **Objective**: Verify dataset contains exactly 50 records
- **Method**: Count rows in the dataset (excluding header)
- **Expected Result**: Total = 50 rows
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 2: Field Presence Validation
- **Objective**: Verify all required fields exist in the dataset
- **Method**: Check for presence of each field name in header row
- **Expected Result**: All 17 fields present:
  - `Loan_ID`
  - `Student_ID`
  - `Age`
  - `Gender`
  - `Race_Ethnicity`
  - `Major`
  - `Graduated`
  - `Disability`
  - `Military`
  - `Employment_Status`
  - `Expected_Annual_Income`
  - `Loan_Type`
  - `Principal_Balance`
  - `Interest_Rate`
  - `Monthly_Payment`
  - `Repayment_Plan`
  - `Default`
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 3: Data Type Validation
- **Objective**: Verify each field contains appropriate data type
- **Method**: Examine data types for each column
- **Expected Result**:
  - Text fields: `Loan_ID`, `Student_ID`, `Gender`, `Race_Ethnicity`, `Major`, `Employment_Status`, `Loan_Type`, `Repayment_Plan`
  - Integer field: `Age`
  - Boolean fields: `Graduated`, `Disability`, `Military`, `Default`
  - Currency fields: `Expected_Annual_Income`, `Principal_Balance`, `Monthly_Payment`
  - Percentage field: `Interest_Rate`
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 4: Age Range Validation
- **Objective**: Verify Age values are within realistic range
- **Method**: Check each Age value
- **Expected Result**: 18 ≤ Age ≤ 65
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 5: Income Validation
- **Objective**: Verify Expected_Annual_Income values are positive
- **Method**: Check each income value
- **Expected Result**: Expected_Annual_Income > 0
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 6: Principal Balance Validation
- **Objective**: Verify Principal_Balance values are positive
- **Method**: Check each principal balance value
- **Expected Result**: Principal_Balance > 0
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 7: Interest Rate Validation
- **Objective**: Verify Interest_Rate values are within realistic range
- **Method**: Check each interest rate value
- **Expected Result**: 0% ≤ Interest_Rate ≤ 20%
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 8: Boolean Field Validation
- **Objective**: Verify boolean fields contain only valid values
- **Method**: Check each boolean field for valid values
- **Expected Result**:
  - `Graduated`: "Yes" or "No"
  - `Disability`: "Yes" or "No"
  - `Military`: "Yes" or "No"
  - `Default`: "Yes" or "No"
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 9: Loan Type Validation
- **Objective**: Verify Loan_Type contains only valid values
- **Method**: Check each Loan_Type value
- **Expected Result**: "Federal" or "Private"
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 10: Employment Status Validation
- **Objective**: Verify Employment_Status contains only valid values
- **Method**: Check each Employment_Status value
- **Expected Result**: "Unemployed", "Part-Time", or "Full-Time"
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 11: Repayment Plan Validation
- **Objective**: Verify Repayment_Plan contains only valid values
- **Method**: Check each Repayment_Plan value
- **Expected Result**: "Standard" or "Income-Driven"
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 12: Gender Field Validation
- **Objective**: Verify Gender field contains only valid values
- **Method**: Check each Gender value
- **Expected Result**: "Male", "Female", or "Non-Binary"
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 13: Race/Ethnicity Field Validation
- **Objective**: Verify Race_Ethnicity field contains valid federal categories
- **Method**: Check each Race_Ethnicity value
- **Expected Result**: Valid federal race/ethnicity categories
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 14: Major Field Validation
- **Objective**: Verify Major field contains valid academic fields
- **Method**: Check each Major value
- **Expected Result**: Valid academic major names
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 15: Default Rate Validation
- **Objective**: Verify default rate is approximately 18%
- **Method**: Calculate percentage of "Yes" values in Default field
- **Expected Result**: Default rate ≈ 18% (9 out of 50 loans)
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

---

## 3. 🧪 Testing Procedure

### Step 1: Dataset Import
1. Import `uchicago_loan_sample.csv` into LibreOffice Calc
2. Verify successful import with no data loss
3. Confirm 50 rows of data (excluding header)

### Step 2: Column Verification
1. Check header row for all required field names
2. Verify column order matches specification
3. Confirm no extra or missing columns

### Step 3: Row-by-Row Validation
1. For each row, validate data types and ranges
2. Check for missing or null values
3. Verify format consistency

### Step 4: Statistical Validation
1. Calculate summary statistics for numeric fields
2. Verify counts for categorical fields
3. Check for outliers or unexpected values

---

## 4. 📊 Validation Checklist

- [ ] Dataset contains exactly 50 rows
- [ ] All 17 required fields present
- [ ] Data types match specification
- [ ] Age values between 18-65
- [ ] Income values positive
- [ ] Principal balance values positive
- [ ] Interest rates between 0-20%
- [ ] Boolean fields contain only "Yes"/"No"
- [ ] Loan Type contains only "Federal"/"Private"
- [ ] Employment Status valid
- [ ] Repayment Plan valid
- [ ] Gender values valid
- [ ] Race/Ethnicity values appropriate
- [ ] Major values appropriate
- [ ] Default rate approximately 18%

---

## 5. 🛠️ Validation Tools

For LibreOffice Calc validation:
- Use COUNTA() function to verify row count
- Use TYPE() function to verify data types
- Use conditional formatting to highlight out-of-range values
- Use filters to examine categorical values
- Use summary functions to calculate statistics

---

## 6. 📝 Expected Output

Upon successful validation, the dataset should:
- Pass all 15 test cases
- Meet all PRD specifications
- Be ready for analysis implementation
- Contain realistic synthetic data
- Support all required calculations and visualizations