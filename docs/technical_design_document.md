# 📋 Technical Design Document (TDD)
**Project Title**: Student Loan Default Risk Analysis – University of Chicago  
**Author**: Urooj Abidi  
**Date**: December 26, 2025  
**Tool**: LibreOffice Calc (v7.6+)  
**License**: MIT (open-source portfolio project)

---

## 1. 🎯 Overview

This Technical Design Document (TDD) outlines the technical approach, implementation steps, and system architecture for the Student Loan Default Risk Analysis project. The document details how to implement a comprehensive risk analysis using LibreOffice Calc, focusing on identifying key predictors of student loan default among University of Chicago-affiliated borrowers.

---

## 2. 🏗️ System Architecture

### 2.1 Technology Stack
| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Primary Tool** | LibreOffice Calc | v7.6+ | Data analysis and visualization |
| **Data Format** | CSV | UTF-8 | Input dataset storage |
| **Output Format** | ODS | OpenDocument | Analysis workbook |
| **Repository** | Git | Any | Version control |
| **Platform** | GitHub | - | Code hosting and documentation |

### 2.2 File Structure
```
/uchicago-student-loan-risk/
├── README.md                 # Project overview, findings, screenshots
├── CHANGELOG.md              # Version history and changes
├── data/
│   └── uchicago_loan_sample.csv
├── analysis/
│   └── uchicago_risk_analysis.ods   # LibreOffice Calc file
└── docs/
    ├── PRD.md                # Product Requirements Document
    ├── TDD.md                # Technical Design Document (this file)
    ├── methodology.md        # EDA steps, assumptions, variable definitions
    └── references.md         # Citations (APA format)
```

---

## 3. 📊 Data Architecture

### 3.1 Input Data Schema
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `Loan_ID` | TEXT | UNIQUE, NOT NULL | Unique identifier |
| `Student_ID` | TEXT | NOT NULL | Anonymized student ID |
| `Age` | INTEGER | 18 ≤ Age ≤ 65 | Borrower age at loan origination |
| `Gender` | TEXT | Enum: Male, Female, Non-Binary | Gender identity |
| `Race_Ethnicity` | TEXT | Enum: Federal categories | For equity analysis |
| `Major` | TEXT | NOT NULL | Field of study |
| `Graduated` | BOOLEAN | Enum: Yes, No | Degree completion status |
| `Disability` | BOOLEAN | Enum: Yes, No | Disability status |
| `Military` | BOOLEAN | Enum: Yes, No | Military service |
| `Employment_Status` | TEXT | Enum: Unemployed, Part-Time, Full-Time | Current employment |
| `Expected_Annual_Income` | CURRENCY | > 0 | Projected post-grad income |
| `Loan_Type` | TEXT | Enum: Federal, Private | Loan category |
| `Principal_Balance` | CURRENCY | > 0 | Initial loan amount |
| `Interest_Rate` | PERCENTAGE | 0 ≤ Rate ≤ 20% | Annual rate |
| `Monthly_Payment` | CURRENCY | ≥ 0 | Estimated payment |
| `Repayment_Plan` | TEXT | Enum: Standard, Income-Driven | Repayment option |
| `Default` | BOOLEAN | Enum: Yes, No | Target variable |

### 3.2 Calculated Fields Schema
| Field | Formula | Purpose |
|-------|---------|---------|
| `Payment_to_Income_Ratio` | `=Monthly_Payment / (Expected_Annual_Income / 12)` | Financial stress indicator |
| `Risk_Score` | `=IF(Graduated="No",2,0) + IF(Loan_Type="Private",3,0) + IF(Expected_Annual_Income<45000,2,0)` | Composite risk measure |
| `Risk_Category` | `=IF(Risk_Score>=5,"High",IF(Risk_Score>=2,"Medium","Low"))` | Risk classification |

---

## 4. 🔧 Implementation Steps

### 4.1 Phase 1: Data Preparation
1. **Generate Synthetic Dataset**
   - Create 50-row CSV file with specified schema
   - Ensure realistic distributions based on college data
   - Balance default rates appropriately (18% as per PRD)

2. **Data Import Process**
   - Import CSV into LibreOffice Calc
   - Validate data types and ranges
   - Clean and format data appropriately

3. **Data Validation**
   - Verify all 50 rows imported correctly
   - Check for missing or invalid values
   - Ensure data types match schema specifications

### 4.2 Phase 2: Formula Implementation
1. **Calculate Payment_to_Income_Ratio**
   - Add formula to new column in spreadsheet
   - Format as percentage
   - Validate calculations with sample data

2. **Calculate Risk_Score**
   - Add formula to new column in spreadsheet
   - Test with various input combinations
   - Verify scoring logic is correct

3. **Calculate Risk_Category**
   - Add formula to new column in spreadsheet
   - Validate category assignments
   - Format for readability

### 4.3 Phase 3: Analysis Implementation
1. **Create PivotTable 1: Default Rate by Graduated**
   - Select relevant data range
   - Configure row fields (Graduated) and column fields (Default)
   - Calculate percentages

2. **Create PivotTable 2: Default Rate by Major**
   - Select relevant data range
   - Configure row fields (Major) and column fields (Default)
   - Calculate percentages

3. **Create PivotTable 3: Avg. Income by Default**
   - Select relevant data range
   - Configure row fields (Default) and value fields (Expected_Annual_Income)
   - Calculate averages

4. **Create PivotTable 4: Default Rate by Loan Type**
   - Select relevant data range
   - Configure row fields (Loan_Type) and column fields (Default)
   - Calculate percentages

### 4.4 Phase 4: Visualization Implementation
1. **Create Bar Chart: Default % by Major**
   - Use PivotTable 2 data
   - Configure as percentage bar chart
   - Add appropriate labels and titles

2. **Create Scatter Plot: Income vs Monthly Payment**
   - Use raw data for X (Income) and Y (Monthly Payment)
   - Color code by Default status
   - Add trend lines if appropriate

3. **Create Pie Chart: Loan Type Distribution**
   - Use Loan_Type counts
   - Configure as pie chart
   - Add percentage labels

### 4.5 Phase 5: Report Generation
1. **Create Summary Report Sheet**
   - Include executive summary text
   - Create key metrics table
   - Add recommendations section

2. **Format Report for Readability**
   - Apply consistent styling
   - Ensure one-page format
   - Add visual hierarchy

### 4.6 Phase 6: Documentation and Deployment
1. **Create Documentation Files**
   - Update README.md with project details
   - Create methodology.md
   - Create references.md with APA citations

2. **Prepare GitHub Repository**
   - Initialize Git repository
   - Create appropriate directory structure
   - Add all required files

3. **Create CHANGELOG.md**
   - Document all changes and versions
   - Follow semantic versioning

---

## 5. 🧮 Technical Specifications

### 5.1 LibreOffice Calc Functions Used
| Function Type | Examples | Purpose |
|---------------|----------|---------|
| **Logical Functions** | IF, AND, OR | Conditional logic for risk scoring |
| **Mathematical Functions** | SUM, AVERAGE, COUNT | Statistical calculations |
| **Lookup Functions** | VLOOKUP, HLOOKUP | Data association (if needed) |
| **Statistical Functions** | MEDIAN, STDEV, CORREL | Advanced analysis |

### 5.2 PivotTable Configuration
| Element | Configuration | Purpose |
|---------|---------------|---------|
| **Row Fields** | Categorical variables (Major, Graduated, etc.) | Grouping data |
| **Column Fields** | Default status | Comparison across categories |
| **Value Fields** | Counts, Averages, Percentages | Quantitative analysis |
| **Filter Fields** | Time periods (if applicable) | Data segmentation |

### 5.3 Chart Specifications
| Chart Type | Data Source | Configuration |
|------------|-------------|---------------|
| **Bar Chart** | PivotTable 2 | Percentage format, color-coded |
| **Scatter Plot** | Raw data | X=Income, Y=Payment, Color=Default |
| **Pie Chart** | Loan Type counts | Percentage format with labels |

---

## 6. ⚠️ Assumptions

### 6.1 Data Assumptions
- The synthetic dataset will follow realistic distributions based on actual college statistics
- The relationships between variables (e.g., graduation rate, loan type, income) reflect real-world patterns
- The sample size of 50 loans is sufficient for exploratory analysis
- The 18% default rate mentioned in the PRD is achievable in the synthetic data

### 6.2 Technical Assumptions
- LibreOffice Calc version 7.6+ is available and functional
- The user has basic familiarity with spreadsheet operations
- The analysis will be performed on a local machine without cloud dependencies
- All formulas and functions used are compatible with LibreOffice Calc

### 6.3 Business Assumptions
- The risk factors identified (non-graduation, private loans, low income) are valid predictors
- The scoring system (Risk_Score) appropriately weights these factors
- The 45K income threshold is a meaningful indicator of risk
- Recommendations will be actionable for financial counselors

### 6.4 Privacy and Ethics Assumptions
- All data used is synthetic and does not contain real personal information
- Race and gender are used only for equity analysis, not for predictive modeling
- The project is clearly labeled as an educational exercise
- No real borrower data is accessed or used

---

## 7. 🧪 Quality Assurance

### 7.1 Data Validation Checks
- Verify dataset contains exactly 50 rows
- Validate all data types match schema specifications
- Check for missing or null values in required fields
- Confirm calculated fields produce expected ranges

### 7.2 Formula Validation
- Test all formulas with known input/output pairs
- Verify conditional logic in Risk_Score and Risk_Category
- Check for division by zero or other mathematical errors
- Validate formatting and display of calculated values

### 7.3 Analysis Validation
- Confirm PivotTables update correctly when data changes
- Verify chart data sources are properly linked
- Test dynamic features for refresh capability
- Ensure all visualizations are readable and informative

---

## 8. 🚀 Deployment Plan

### 8.1 Pre-deployment Checklist
- [ ] All formulas and calculations validated
- [ ] PivotTables and charts functional
- [ ] Summary report complete and accurate
- [ ] Documentation files created
- [ ] GitHub repository structure complete

### 8.2 GitHub Repository Setup
1. Initialize local Git repository
2. Add all project files
3. Create initial commit with comprehensive message
4. Push to GitHub remote repository
5. Verify all files are properly committed and pushed

### 8.3 Final Validation
- Open ODS file in LibreOffice Calc to verify functionality
- Test all interactive elements (PivotTables, charts)
- Verify all documentation is accurate and complete
- Confirm README.md includes required screenshots and information

---

## 9. 📈 Success Criteria

The technical implementation is successful when:
- [ ] LibreOffice Calc file opens without errors
- [ ] All 50 rows of data are properly loaded and formatted
- [ ] All calculated fields (Risk_Score, Risk_Category, etc.) function correctly
- [ ] All 4 PivotTables display accurate information
- [ ] All 3 charts visualize data effectively
- [ ] Summary report contains accurate metrics as specified in PRD
- [ ] GitHub repository contains all required files and documentation
- [ ] README.md includes screenshots and proper project description
- [ ] CHANGELOG.md documents the development process
- [ ] All formulas are properly documented

---

## 10. 🔧 Troubleshooting Guide

### 10.1 Common Issues and Solutions
| Issue | Solution |
|-------|----------|
| **Formulas not calculating** | Check cell formatting, ensure formula syntax is correct |
| **PivotTables not updating** | Verify data range, refresh PivotTable manually |
| **Charts not displaying data** | Check data source links, verify chart configuration |
| **File won't open in Calc** | Verify ODS format, check for special characters |

### 10.2 Performance Considerations
- With only 50 rows, performance should not be an issue
- Limit complex array formulas to maintain responsiveness
- Use appropriate data types to optimize calculation speed