# 📊 PivotTable and Chart Tests

**Repository**: https://github.com/Uroojabidi/Finance-Portfolio/
**Project Title**: Student Loan Default Risk Analysis – University of Chicago
**Author**: Urooj Abidi
**Email**: uroojabid203@gmail.com
**Date**: December 26, 2025
**Tool**: Python CLI Application
**License**: MIT (open-source portfolio project)

---

## 1. 🎯 Test Overview

This document outlines the validation tests for the PivotTables and charts in the student loan risk analysis project. These tests ensure that all visualizations accurately represent the data and provide meaningful insights.

---

## 2. 📋 PivotTable Specifications

### PivotTable 1: Default Rate by Graduated
- **Rows**: Graduated (Yes/No)
- **Columns**: Default (Yes/No)
- **Values**: Count of records, formatted as percentages
- **Purpose**: Show relationship between graduation status and default rate

### PivotTable 2: Default Rate by Major
- **Rows**: Major (various fields of study)
- **Columns**: Default (Yes/No)
- **Values**: Count of records, formatted as percentages
- **Purpose**: Identify fields of study with higher default rates

### PivotTable 3: Avg. Income by Default
- **Rows**: Default (Yes/No)
- **Values**: Average of Expected_Annual_Income
- **Purpose**: Compare income levels between defaulted and repaid loans

### PivotTable 4: Default Rate by Loan Type
- **Rows**: Loan_Type (Federal/Private)
- **Columns**: Default (Yes/No)
- **Values**: Count of records, formatted as percentages
- **Purpose**: Analyze differences between federal and private loans

---

## 3. 📊 Chart Specifications

### Chart 1: Bar Chart - Default % by Major
- **Type**: Clustered bar chart
- **X-Axis**: Major
- **Y-Axis**: Default percentage
- **Purpose**: Visualize default rates across different fields of study

### Chart 2: Scatter Plot - Income vs Monthly Payment
- **Type**: XY (Scatter) chart
- **X-Axis**: Expected_Annual_Income
- **Y-Axis**: Monthly_Payment
- **Color**: Default status (Yes/No)
- **Purpose**: Show relationship between income and payment burden

### Chart 3: Pie Chart - Loan Type Distribution
- **Type**: Pie chart
- **Data**: Count of Federal vs Private loans
- **Purpose**: Display proportion of loan types in the sample

---

## 4. 🧪 Test Cases

### Test Case 1: PivotTable 1 - Default Rate by Graduated
- **Objective**: Verify correct calculation of default rates by graduation status
- **Method**: Check pivot table against manual calculations
- **Expected Result**: Non-graduates should have higher default rate (as specified in PRD: 67%)
- **Validation Steps**:
  1. Count total graduates and non-graduates
  2. Count defaults among each group
  3. Calculate percentage rates
  4. Compare to pivot table values
- **Expected Values**:
  - Graduated="Yes": Lower default rate
  - Graduated="No": Higher default rate (≈67%)
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 2: PivotTable 2 - Default Rate by Major
- **Objective**: Verify correct calculation of default rates by major
- **Method**: Check pivot table against manual calculations
- **Expected Result**: Some majors should show higher default rates than others
- **Validation Steps**:
  1. Group records by major
  2. Count defaults within each major
  3. Calculate percentage rates
  4. Compare to pivot table values
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 3: PivotTable 3 - Avg. Income by Default
- **Objective**: Verify correct calculation of average income by default status
- **Method**: Check pivot table against manual calculations
- **Expected Result**: 
  - Default="Yes": Lower average income (as specified in PRD: $36,200)
  - Default="No": Higher average income (as specified in PRD: $82,500)
- **Validation Steps**:
  1. Separate records by default status
  2. Calculate average income for each group
  3. Compare to pivot table values
- **Expected Values**:
  - Default="Yes": ≈$36,200
  - Default="No": ≈$82,500
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 4: PivotTable 4 - Default Rate by Loan Type
- **Objective**: Verify correct calculation of default rates by loan type
- **Method**: Check pivot table against manual calculations
- **Expected Result**: Private loans should have higher default rate than federal loans
- **Validation Steps**:
  1. Group records by loan type
  2. Count defaults within each type
  3. Calculate percentage rates
  4. Compare to pivot table values
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 5: Chart 1 - Bar Chart Accuracy
- **Objective**: Verify bar chart accurately represents PivotTable 2 data
- **Method**: Compare chart values to PivotTable 2 values
- **Expected Result**: Chart bars should match PivotTable percentages
- **Validation Steps**:
  1. Extract data from PivotTable 2
  2. Compare to chart Y-axis values
  3. Verify all majors are represented
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 6: Chart 2 - Scatter Plot Accuracy
- **Objective**: Verify scatter plot correctly plots income vs payment
- **Method**: Check random points against raw data values
- **Expected Result**: Each point should represent one record with correct coordinates
- **Validation Steps**:
  1. Select random data points
  2. Verify coordinates match raw data
  3. Check color coding by default status
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 7: Chart 3 - Pie Chart Accuracy
- **Objective**: Verify pie chart correctly represents loan type distribution
- **Method**: Compare chart percentages to raw data counts
- **Expected Result**: Pie segments should match proportion of federal vs private loans
- **Validation Steps**:
  1. Count federal vs private loans in raw data
  2. Calculate percentages
  3. Compare to pie chart segments
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 8: Dynamic Update Test
- **Objective**: Verify PivotTables and charts update when underlying data changes
- **Method**: Temporarily modify a few data values and check if visualizations update
- **Expected Result**: All PivotTables and charts should automatically update
- **Validation Steps**:
  1. Change a few values in raw data
  2. Verify PivotTables refresh automatically
  3. Verify charts update accordingly
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 9: Formatting and Labels
- **Objective**: Verify all visualizations have proper formatting and labels
- **Method**: Check each chart and PivotTable for completeness
- **Expected Result**: All visualizations should have:
  - Clear titles
  - Proper axis labels
  - Legible fonts
  - Appropriate colors
  - Accurate data representation
- **Validation Steps**:
  1. Check chart titles are descriptive
  2. Verify axis labels are clear
  3. Confirm legend is present where needed
  4. Ensure fonts are readable
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

### Test Case 10: Summary Report Integration
- **Objective**: Verify PivotTable data supports summary report metrics
- **Method**: Check that key metrics in summary report match PivotTable calculations
- **Expected Result**: Summary report metrics should match PivotTable values:
  - Total Loans: 50
  - Default Rate: 18%
  - Avg. Income (Default): $36,200
  - Avg. Income (Paid): $82,500
  - Default Rate (Not Graduated): 67%
- **Validation Steps**:
  1. Extract metrics from PivotTables
  2. Compare to summary report values
  3. Verify consistency across all metrics
- **Status**: [PENDING]
- **Pass/Fail**: [TBD]

---

## 5. 🧪 Testing Procedure

### Step 1: PivotTable Creation
1. Create each PivotTable as specified
2. Verify correct field placement
3. Confirm value calculations are accurate

### Step 2: Chart Creation
1. Create each chart based on PivotTable or raw data
2. Apply appropriate formatting
3. Verify data representation is accurate

### Step 3: Accuracy Testing
1. Manually verify random values in each PivotTable
2. Cross-check chart values against PivotTable data
3. Confirm all calculations match expectations

### Step 4: Dynamic Testing
1. Make minor changes to source data
2. Verify all PivotTables and charts update correctly
3. Confirm no broken links or errors occur

### Step 5: Integration Testing
1. Verify all components work together
2. Check that summary report reflects analysis
3. Confirm all project requirements are met

---

## 6. 📊 Validation Checklist

- [ ] All 4 PivotTables created correctly
- [ ] All 3 charts created correctly
- [ ] PivotTable values match manual calculations
- [ ] Chart values match PivotTable data
- [ ] All visualizations update dynamically
- [ ] Proper formatting and labeling applied
- [ ] Summary report metrics align with visualizations
- [ ] Visualizations provide meaningful insights
- [ ] All visualizations are readable and clear
- [ ] Charts support the project's analytical goals

---

## 7. 🛠️ Validation Tools

For LibreOffice Calc validation:
- Use manual calculations to verify PivotTable results
- Apply data filters to isolate specific segments
- Use conditional formatting to highlight key values
- Test refresh functionality of PivotTables
- Verify chart data source links

---

## 8. 📝 Expected Output

Upon successful validation, the PivotTables and charts should:
- Pass all 10 test cases
- Accurately represent the underlying data
- Provide clear insights into loan default risk factors
- Update dynamically when source data changes
- Support the executive summary and recommendations
- Meet all PRD visualization requirements