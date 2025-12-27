# 🧮 Calculated Fields Tests

**Repository**: https://github.com/Uroojabidi/Finance-Portfolio/
**Project Title**: Student Loan Default Risk Analysis – University of Chicago
**Author**: Urooj Abidi
**Email**: uroojabid203@gmail.com
**Date**: December 26, 2025
**Tool**: Python CLI Application
**License**: MIT (open-source portfolio project)

---

## 1. 🎯 Test Overview

This document outlines the validation tests for the calculated fields in the student loan risk analysis project. These tests ensure that all formulas produce accurate and expected results.

---

## 2. 📋 Calculated Fields Specification

### Field 1: Payment_to_Income_Ratio
- **Formula**: `=Monthly_Payment / (Expected_Annual_Income / 12)`
- **Purpose**: Measures the financial burden of loan payments relative to income
- **Expected Range**: Typically 0.01 to 0.50 (1% to 50%)

### Field 2: Risk_Score
- **Formula**: `=IF(Graduated="No",2,0) + IF(Loan_Type="Private",3,0) + IF(Expected_Annual_Income<45000,2,0)`
- **Purpose**: Combines multiple risk factors into a composite score
- **Expected Range**: 0 to 7

### Field 3: Risk_Category
- **Formula**: `=IF(Risk_Score>=5,"High",IF(Risk_Score>=2,"Medium","Low"))`
- **Purpose**: Categorizes risk levels for easier interpretation
- **Expected Values**: "High", "Medium", or "Low"

---

## 3. 🧪 Test Cases

### Test Case 1: Payment_to_Income_Ratio Calculation
- **Objective**: Verify correct calculation of payment-to-income ratio
- **Method**: Apply formula to sample data and verify result
- **Sample Input**: Monthly_Payment = $340, Expected_Annual_Income = $48,000
- **Expected Result**: 340 / (48000/12) = 340 / 4000 = 0.085 or 8.5%
- **Test Data**:
  | Monthly_Payment | Expected_Annual_Income | Expected Ratio | Actual Result | Pass/Fail |
  |-----------------|------------------------|----------------|---------------|-----------|
  | $340 | $48,000 | 0.085 | [TBD] | [TBD] |
  | $500 | $60,000 | 0.100 | [TBD] | [TBD] |
  | $200 | $36,000 | 0.067 | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 2: Risk_Score Calculation - Graduation Factor
- **Objective**: Verify graduation status adds 2 points for non-graduates
- **Method**: Test with various graduation statuses
- **Sample Input**: Graduated="No", Loan_Type="Federal", Income=$50,000
- **Expected Result**: 2 + 0 + 0 = 2
- **Test Data**:
  | Graduated | Loan_Type | Income | Expected Score | Actual Result | Pass/Fail |
  |-----------|-----------|--------|----------------|---------------|-----------|
  | No | Federal | $50,000 | 2 | [TBD] | [TBD] |
  | Yes | Federal | $50,000 | 0 | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 3: Risk_Score Calculation - Loan Type Factor
- **Objective**: Verify private loans add 3 points
- **Method**: Test with different loan types
- **Sample Input**: Graduated="Yes", Loan_Type="Private", Income=$50,000
- **Expected Result**: 0 + 3 + 0 = 3
- **Test Data**:
  | Graduated | Loan_Type | Income | Expected Score | Actual Result | Pass/Fail |
  |-----------|-----------|--------|----------------|---------------|-----------|
  | Yes | Private | $50,000 | 3 | [TBD] | [TBD] |
  | Yes | Federal | $50,000 | 0 | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 4: Risk_Score Calculation - Income Factor
- **Objective**: Verify income below $45,000 adds 2 points
- **Method**: Test with different income levels
- **Sample Input**: Graduated="Yes", Loan_Type="Federal", Income=$40,000
- **Expected Result**: 0 + 0 + 2 = 2
- **Test Data**:
  | Graduated | Loan_Type | Income | Expected Score | Actual Result | Pass/Fail |
  |-----------|-----------|--------|----------------|---------------|-----------|
  | Yes | Federal | $40,000 | 2 | [TBD] | [TBD] |
  | Yes | Federal | $50,000 | 0 | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 5: Risk_Score Calculation - Combined Factors
- **Objective**: Verify all factors combine correctly
- **Method**: Test with all risk factors present
- **Sample Input**: Graduated="No", Loan_Type="Private", Income=$40,000
- **Expected Result**: 2 + 3 + 2 = 7
- **Test Data**:
  | Graduated | Loan_Type | Income | Expected Score | Actual Result | Pass/Fail |
  |-----------|-----------|--------|----------------|---------------|-----------|
  | No | Private | $40,000 | 7 | [TBD] | [TBD] |
  | No | Private | $50,000 | 5 | [TBD] | [TBD] |
  | No | Federal | $40,000 | 4 | [TBD] | [TBD] |
  | Yes | Federal | $30,000 | 2 | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 6: Risk_Category Assignment - High Risk
- **Objective**: Verify Risk_Score ≥ 5 results in "High" category
- **Method**: Test with scores of 5 and above
- **Sample Input**: Risk_Score = 5
- **Expected Result**: "High"
- **Test Data**:
  | Risk_Score | Expected Category | Actual Result | Pass/Fail |
  |------------|-------------------|---------------|-----------|
  | 5 | High | [TBD] | [TBD] |
  | 6 | High | [TBD] | [TBD] |
  | 7 | High | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 7: Risk_Category Assignment - Medium Risk
- **Objective**: Verify Risk_Score ≥ 2 and < 5 results in "Medium" category
- **Method**: Test with scores of 2-4
- **Sample Input**: Risk_Score = 3
- **Expected Result**: "Medium"
- **Test Data**:
  | Risk_Score | Expected Category | Actual Result | Pass/Fail |
  |------------|-------------------|---------------|-----------|
  | 2 | Medium | [TBD] | [TBD] |
  | 3 | Medium | [TBD] | [TBD] |
  | 4 | Medium | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 8: Risk_Category Assignment - Low Risk
- **Objective**: Verify Risk_Score < 2 results in "Low" category
- **Method**: Test with scores of 0-1
- **Sample Input**: Risk_Score = 1
- **Expected Result**: "Low"
- **Test Data**:
  | Risk_Score | Expected Category | Actual Result | Pass/Fail |
  |------------|-------------------|---------------|-----------|
  | 0 | Low | [TBD] | [TBD] |
  | 1 | Low | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 9: Formula Error Handling
- **Objective**: Verify formulas handle edge cases gracefully
- **Method**: Test with invalid or missing data
- **Expected Result**: Appropriate error handling or null values
- **Test Data**:
  | Monthly_Payment | Income | Expected Behavior | Actual Result | Pass/Fail |
  |-----------------|--------|-------------------|---------------|-----------|
  | $0 | $50,000 | 0.000 | [TBD] | [TBD] |
  | $300 | $0 | Error or #DIV/0 | [TBD] | [TBD] |
- **Status**: [PENDING]

### Test Case 10: Range Validation for Calculated Fields
- **Objective**: Verify calculated fields produce expected ranges
- **Method**: Validate output ranges for all calculated fields
- **Expected Results**:
  - Payment_to_Income_Ratio: Should be non-negative
  - Risk_Score: Should be integer between 0 and 7
  - Risk_Category: Should be "High", "Medium", or "Low"
- **Status**: [PENDING]

---

## 4. 🧪 Testing Procedure

### Step 1: Formula Implementation
1. Add calculated field columns to the dataset
2. Implement formulas as specified
3. Verify formulas copy correctly to all rows

### Step 2: Sample Testing
1. Apply formulas to sample data points
2. Verify individual calculations match expected results
3. Check for formula errors or inconsistencies

### Step 3: Full Dataset Testing
1. Apply formulas to all 50 records
2. Verify all calculations complete without errors
3. Validate output ranges and distributions

### Step 4: Cross-Validation
1. Manually calculate several values to verify formula accuracy
2. Check for consistency across all records
3. Validate risk category distributions make sense

---

## 5. 📊 Validation Checklist

- [ ] Payment_to_Income_Ratio formula implemented correctly
- [ ] Risk_Score formula accounts for all three factors
- [ ] Risk_Category formula correctly categorizes scores
- [ ] All formulas apply to all 50 records
- [ ] No formula errors in the dataset
- [ ] Calculated values fall within expected ranges
- [ ] Risk categories distribute reasonably across the dataset
- [ ] Formulas update dynamically if input values change

---

## 6. 🛠️ Validation Tools

For LibreOffice Calc validation:
- Use manual calculations to verify formula accuracy
- Apply conditional formatting to highlight unexpected values
- Use data validation to ensure proper output formats
- Create test rows with known inputs and expected outputs
- Use summary functions to validate distributions

---

## 7. 📝 Expected Output

Upon successful validation, the calculated fields should:
- Pass all 10 test cases
- Produce accurate and consistent results
- Support all downstream analysis requirements
- Be properly documented for reproducibility
- Enable effective risk categorization and analysis