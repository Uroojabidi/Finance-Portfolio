# 📋 Methodology Document

**Repository**: https://github.com/Uroojabidi/Finance-Portfolio/
**Project Title**: Student Loan Default Risk Analysis – University of Chicago
**Author**: Urooj Abidi
**Email**: uroojabid203@gmail.com
**Date**: December 26, 2025
**Tool**: Python CLI Application
**License**: MIT (open-source portfolio project)

---

## 1. 🎯 Purpose

This methodology document outlines the approach, techniques, and validation methods used in the Student Loan Default Risk Analysis project. It serves as a guide for understanding the analytical process, data handling, and risk assessment methodologies implemented in this educational project.

---

## 2. 🧪 Analytical Approach

### 2.1 Exploratory Data Analysis (EDA)
The project employs descriptive statistical methods to understand patterns in student loan data:

- **Univariate Analysis**: Examining distributions of individual variables (age, income, loan amount)
- **Bivariate Analysis**: Investigating relationships between pairs of variables (default rate vs graduation status)
- **Multivariate Analysis**: Assessing complex relationships between multiple variables simultaneously

### 2.2 Risk Assessment Methodology
Risk is assessed using a composite scoring system that combines multiple risk factors:

1. **Graduation Status**: Non-graduates receive 2 points (higher risk)
2. **Loan Type**: Private loans receive 3 points (higher risk)
3. **Income Level**: Income below $45,000 receives 2 points (higher risk)

The composite risk score determines the risk category:
- **High Risk**: Score ≥ 5
- **Medium Risk**: Score ≥ 2
- **Low Risk**: Score < 2

---

## 3. 📊 Data Handling Methodology

### 3.1 Data Collection
- **Synthetic Data Generation**: All data is artificially generated to simulate real-world patterns
- **Variable Selection**: Variables selected based on known risk factors for loan default
- **Sample Size**: 50 records to provide sufficient data for analysis while maintaining manageability

### 3.2 Data Validation
- **Range Checks**: Ensuring values fall within realistic ranges
- **Format Validation**: Verifying data types match expected formats
- **Completeness Checks**: Confirming all required fields are populated

### 3.3 Data Transformation
- **Calculated Fields**: Creating derived metrics like payment-to-income ratio
- **Categorization**: Converting continuous variables to categorical where appropriate
- **Normalization**: Standardizing formats for consistency

---

## 4. 📈 Analysis Techniques

### 4.1 PivotTable Analysis
PivotTables are used to examine relationships between categorical variables:

- **Default Rate by Graduation Status**: Comparing default rates between graduates and non-graduates
- **Default Rate by Major**: Identifying fields of study with higher default rates
- **Average Income by Default Status**: Comparing income levels between defaulted and repaid loans
- **Default Rate by Loan Type**: Analyzing differences between federal and private loans

### 4.2 Visualization Techniques
- **Bar Charts**: For comparing categorical data (default rates by major)
- **Scatter Plots**: For examining relationships between continuous variables (income vs payment)
- **Pie Charts**: For showing proportional distributions (loan type distribution)

---

## 5. 🧮 Calculated Fields Methodology

### 5.1 Payment-to-Income Ratio
**Formula**: `=Monthly_Payment / (Expected_Annual_Income / 12)`

**Purpose**: Measures the financial burden of loan payments relative to income, indicating potential stress.

### 5.2 Risk Score Calculation
**Formula**: `=IF(Graduated="No",2,0) + IF(Loan_Type="Private",3,0) + IF(Expected_Annual_Income<45000,2,0)`

**Purpose**: Combines multiple risk factors into a single composite score for risk assessment.

### 5.3 Risk Category Assignment
**Formula**: `=IF(Risk_Score>=5,"High",IF(Risk_Score>=2,"Medium","Low"))`

**Purpose**: Translates the continuous risk score into discrete risk categories for easier interpretation.

---

## 6. ✅ Validation and Quality Assurance

### 6.1 Data Validation Checks
- **Row Count Validation**: Confirming exactly 50 records exist
- **Data Type Validation**: Ensuring each field contains appropriate data types
- **Range Validation**: Verifying values fall within expected ranges
- **Formula Validation**: Confirming calculated fields produce expected results

### 6.2 Analysis Validation
- **Cross-verification**: Checking that PivotTable results match manual calculations
- **Consistency Checks**: Ensuring calculations are consistent across all records
- **Reasonableness Checks**: Verifying that results align with expected patterns

---

## 7. 🎓 Educational Focus

### 7.1 Learning Objectives
- Demonstrate proficiency with spreadsheet-based data analysis
- Illustrate risk assessment methodologies
- Showcase exploratory data analysis techniques
- Apply statistical concepts to real-world scenarios

### 7.2 Skills Demonstrated
- Data manipulation and cleaning
- Formula creation and validation
- PivotTable creation and interpretation
- Data visualization techniques
- Risk modeling and assessment

---

## 8. 🔒 Ethical Considerations

### 8.1 Privacy and Data Security
- All data is synthetic and does not contain real personal information
- No actual borrower data is used or accessed
- Project clearly labeled as synthetic educational exercise

### 8.2 Bias and Fairness
- Race and gender variables used only for equity analysis, not prediction
- Focus on educational demonstration rather than actual risk assessment
- Emphasis on ethical data use and interpretation

---

## 9. 📚 References and Standards

This methodology aligns with:
- Best practices in financial risk analysis
- Ethical guidelines for data analysis
- Educational standards for portfolio projects
- Open-source software utilization (LibreOffice Calc)

---

## 10. 🔄 Continuous Improvement

The methodology will be refined based on:
- Feedback from analysis results
- Validation of calculated metrics
- Assessment of visualization effectiveness
- Alignment with project requirements