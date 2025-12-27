# 📋 Technical Design Document (TDD)
**Repository**: https://github.com/Uroojabidi/Finance-Portfolio/
**Project Title**: Student Loan Default Risk Analysis – University of Chicago
**Author**: Urooj Abidi
**Email**: uroojabid203@gmail.com
**Date**: December 26, 2025
**Tool**: Python CLI Application
**License**: MIT (open-source portfolio project)

---

## 📋 Table of Contents
- [Overview](#-overview)
- [System Architecture](#-system-architecture)
- [Data Architecture](#-data-architecture)
- [Implementation Steps](#-implementation-steps)
- [Technical Specifications](#-technical-specifications)
- [Assumptions](#-assumptions)
- [Quality Assurance](#-quality-assurance)
- [Deployment Plan](#-deployment-plan)
- [Success Criteria](#-success-criteria)
- [Troubleshooting Guide](#-troubleshooting-guide)

---

## 1. 🎯 Overview

This Technical Design Document (TDD) outlines the technical approach, implementation steps, and system architecture for the Student Loan Default Risk Analysis project. The document details how to implement a comprehensive risk analysis using a Python CLI application, focusing on identifying key predictors of student loan default among University of Chicago-affiliated borrowers.

---

## 2. 🏗️ System Architecture

### 2.1 Architecture Diagram
View the system architecture diagram [here](../diagram/architecture.mmd).

### 2.2 Technology Stack
| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Primary Tool** | Python | 3.7+ | Data analysis and risk assessment |
| **Data Processing** | pandas | 1.3+ | Data manipulation and analysis |
| **CLI Framework** | argparse | Built-in | Command-line argument parsing |
| **Data Format** | CSV | UTF-8 | Input/output data storage |
| **Repository** | Git | Any | Version control |
| **Platform** | GitHub | - | Code hosting and documentation |

### 2.3 File Structure
```
/uchicago-student-loan-risk/
├── README.md                 # Project overview, usage instructions
├── risk_analyzer.py          # Main Python CLI application
├── requirements.txt          # Python dependencies
├── data/
│   └── Qwen_csv_20251225_upsmabt6b.csv
├── output/
│   └── risk_report.csv       # Risk analysis output
└── docs/
    ├── PRD.md                # Product Requirements Document
    ├── technical_design_document.md # Technical Design Document (this file)
    ├── diagram/              # Architecture diagrams
    │   └── architecture.mmd  # System architecture diagram
    ├── methodology.md        # EDA steps, assumptions, variable definitions
    └── references.md         # Citations (APA format)
```

---

## 3. 📊 Data Architecture

### 3.1 Input Data Schema
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `Loan_ID` | TEXT | UNIQUE, NOT NULL | Unique identifier |
| `Age` | INTEGER | 18 ≤ Age ≤ 65 | Borrower age at loan origination |
| `Citizenship` | TEXT | Enum: U.S., International | Citizenship status |
| `Major` | TEXT | NOT NULL | Field of study |
| `Degree_Level` | TEXT | Enum: Bachelor, Master, PhD, JD | Educational level |
| `Expected_Income` | INTEGER | > 0 | Projected post-grad income |
| `Employment_Status` | TEXT | Enum: Employed, Unemployed | Current employment |
| `Credit_Score` | INTEGER or N/A | ≥ 300 if present | Credit score (if available) |
| `Loan_Amount` | INTEGER | > 0 | Loan principal amount |
| `Interest_Rate` | FLOAT | 0 ≤ Rate ≤ 20% | Annual interest rate |
| `Monthly_Payment` | INTEGER | ≥ 0 | Estimated monthly payment |
| `DTI_Ratio` | FLOAT | ≥ 0 | Debt-to-income ratio |
| `Has_Cosigner` | TEXT | Enum: Yes, No | Cosigner presence |
| `Default` | TEXT | Enum: Yes, No | Target variable |

### 3.2 Calculated Fields Schema
| Field | Python Calculation | Purpose |
|-------|----------------------|---------|
| `Payment_to_Income_Ratio` | `Monthly_Payment / (Expected_Income / 12)` | Financial stress indicator |
| `Risk_Score` | Weighted sum of risk factors | Composite risk measure |
| `Risk_Category` | Categorized based on Risk_Score | Risk classification |

---

## 4. 🔧 Implementation Steps

### 4.1 Phase 1: Environment Setup
1. **Create Python project structure**
   - Set up virtual environment
   - Install required dependencies (pandas, argparse)
   - Create requirements.txt

2. **Initialize project files**
   - Create main application file (risk_analyzer.py)
   - Set up directory structure
   - Create initial documentation

### 4.2 Phase 2: Data Loading and Validation
1. **Implement CSV loading functionality**
   - Use pandas to read CSV file
   - Validate required columns exist
   - Check data types and ranges

2. **Implement data validation**
   - Verify all required fields are present
   - Check for missing or invalid values
   - Ensure data types match schema specifications

### 4.3 Phase 3: Risk Calculation Implementation
1. **Calculate Payment_to_Income_Ratio**
   - Add calculated column to DataFrame
   - Handle division by zero cases
   - Validate calculations with sample data

2. **Calculate Risk_Score**
   - Implement weighted risk factor calculation
   - Test with various input combinations
   - Verify scoring logic is correct

3. **Calculate Risk_Category**
   - Implement category assignment based on thresholds
   - Validate category assignments
   - Format for readability

### 4.4 Phase 4: Analysis Implementation
1. **Implement Summary Statistics**
   - Calculate overall default rate
   - Compute key metrics (average income, loan amounts, etc.)
   - Generate statistical summaries

2. **Implement Risk Factor Analysis**
   - Analyze default rates by major
   - Analyze default rates by employment status
   - Analyze default rates by citizenship
   - Analyze default rates by degree level

### 4.5 Phase 5: Output Generation
1. **Create risk analysis report**
   - Generate CSV output with comprehensive analysis
   - Include individual risk assessments
   - Add summary statistics and key findings

2. **Format output for readability**
   - Apply consistent formatting
   - Ensure CSV structure is well-organized
   - Add headers and descriptions

### 4.6 Phase 6: CLI Interface Implementation
1. **Implement command-line argument parsing**
   - Input file path
   - Output file path
   - Optional verbose mode

2. **Create main application flow**
   - Load data from specified input file
   - Perform risk analysis
   - Generate output report
   - Provide console feedback

---

## 5. 🧮 Technical Specifications

### 5.1 Python Libraries Used
| Library | Purpose | Functions Used |
|---------|---------|----------------|
| **pandas** | Data manipulation | DataFrame, read_csv, groupby, describe |
| **argparse** | CLI argument parsing | ArgumentParser |
| **sys** | System-specific parameters | exit, stderr |
| **os** | Operating system interface | path operations |

### 5.2 Risk Scoring Algorithm
| Factor | Weight | Condition |
|--------|--------|-----------|
| Employment Status | 3 points | Unemployed = 3, Employed = 0 |
| Expected Income | 2 points | < $45,000 = 2, ≥ $45,000 = 0 |
| DTI Ratio | 2 points | > 0.20 = 2, ≤ 0.20 = 0 |
| Credit Score | 1 point | < 600 = 1, ≥ 600 or N/A = 0 |
| Citizenship | 1 point | International = 1, U.S. = 0 |
| Degree Level | 1 point | Bachelor = 1, Master = 0, PhD = 0, JD = 0 |

### 5.3 Risk Category Thresholds
| Category | Score Range |
|----------|-------------|
| **Low Risk** | Score < 2 |
| **Medium Risk** | 2 ≤ Score ≤ 4 |
| **High Risk** | Score > 4 |

---

## 6. ⚠️ Assumptions

### 6.1 Data Assumptions
- The input CSV will follow the specified schema
- The relationships between variables reflect real-world patterns
- Missing credit scores (N/A) are treated as neutral risk factors
- The provided dataset is representative of the population being analyzed

### 6.2 Technical Assumptions
- Python 3.7+ is available on the target system
- The user has basic familiarity with command-line interfaces
- The analysis will be performed on a local machine
- CSV files are properly formatted and accessible

### 6.3 Business Assumptions
- The risk factors identified are valid predictors of default
- The scoring system appropriately weights different risk factors
- The thresholds for risk categories are meaningful
- Recommendations will be actionable for financial counselors

### 6.4 Privacy and Ethics Assumptions
- All data used is synthetic and does not contain real personal information
- The project is clearly labeled as an educational exercise
- No real borrower data is accessed or used

---

## 7. 🧪 Quality Assurance

### 7.1 Data Validation Checks
- Verify required columns exist in input CSV
- Validate data types match expected schema
- Check for missing or null values in critical fields
- Confirm calculated fields produce expected ranges

### 7.2 Risk Calculation Validation
- Test risk scoring with known input/output pairs
- Verify all risk factors are properly weighted
- Check for division by zero or other mathematical errors
- Validate risk category assignments

### 7.3 Output Validation
- Confirm CSV output is properly formatted
- Verify all required analysis components are included
- Test with various input files to ensure robustness
- Ensure console output is informative and clear

### 7.4 Testing Strategy
The application implements a comprehensive testing strategy with 19 unit and integration tests:

#### Risk Calculation Tests
- `test_calculate_risk_score_employed_low_income`: Validates risk score calculation for employed person with low income
- `test_calculate_risk_score_unemployed`: Validates risk score calculation for unemployed person
- `test_calculate_risk_score_high_dti`: Validates risk score calculation for high DTI ratio
- `test_calculate_risk_score_low_credit`: Validates risk score calculation for low credit score
- `test_calculate_risk_score_international`: Validates risk score calculation for international student
- `test_calculate_risk_score_all_factors`: Validates risk score calculation with all risk factors
- `test_assign_risk_category_low`: Validates risk category assignment for low risk scores
- `test_assign_risk_category_medium`: Validates risk category assignment for medium risk scores
- `test_assign_risk_category_high`: Validates risk category assignment for high risk scores

#### Risk Calculation Utility Tests
- `test_calculate_payment_to_income_ratio`: Validates payment-to-income ratio calculation
- `test_calculate_payment_to_income_ratio_zero_income`: Validates payment-to-income ratio with zero income

#### Data Loading and Validation Tests
- `test_load_and_validate_data_success`: Validates successful loading and validation of data
- `test_load_and_validate_data_missing_file`: Tests error handling for missing file
- `test_load_and_validate_data_missing_columns`: Tests error handling for missing required columns

#### Analysis Function Tests
- `test_perform_analysis`: Validates the perform_analysis function

#### CLI Functionality Tests
- `test_main_function_calls`: Validates that main function calls the right functions

#### Integration Tests
- `test_load_real_csv_files`: Validates loading all real CSV files
- `test_perform_analysis_on_real_data`: Validates performing analysis on real data
- `test_risk_distribution_in_real_data`: Validates risk distribution in real data

#### Test Execution
Tests can be executed using:
```bash
python -m unittest discover tests/ -v
```

---

## 8. 🚀 Deployment Plan

### 8.1 Pre-deployment Checklist
- [ ] Python application runs without errors
- [ ] Risk calculations are accurate and consistent
- [ ] Output CSV contains all required information
- [ ] Documentation files created and updated
- [ ] GitHub repository structure complete

### 8.2 GitHub Repository Setup
1. Initialize local Git repository
2. Add all project files
3. Create initial commit with comprehensive message
4. Push to GitHub remote repository
5. Verify all files are properly committed and pushed

### 8.3 Final Validation
- Run application with sample data to verify functionality
- Test CLI argument parsing
- Verify output CSV structure and content
- Confirm README.md includes required usage instructions

---

## 9. 📈 Success Criteria

The technical implementation is successful when:
- [ ] Python CLI application processes input CSV correctly
- [ ] Risk analysis report is generated in CSV format
- [ ] All calculated fields (Risk_Score, Risk_Category, etc.) function correctly
- [ ] Risk factor analysis provides meaningful insights
- [ ] Output contains accurate metrics as specified in PRD
- [ ] GitHub repository contains all required files and documentation
- [ ] README.md includes usage instructions and project description
- [ ] All calculations are properly documented and reproducible

---

## 10. 🔧 Troubleshooting Guide

### 10.1 Common Issues and Solutions
| Issue | Solution |
|-------|----------|
| **CSV file not found** | Verify file path is correct and file exists |
| **Missing required columns** | Ensure input CSV matches expected schema |
| **Python dependencies missing** | Install required packages using pip and requirements.txt |
| **Permission errors** | Check file permissions for read/write access |

### 10.2 Performance Considerations
- For large datasets, pandas operations are optimized for efficiency
- Memory usage is minimized by processing data in appropriate chunks
- Calculations are vectorized for optimal performance