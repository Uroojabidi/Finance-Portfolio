# 📄 Product Requirements Document (PRD)
**Repository**: https://github.com/Uroojabidi/Finance-Portfolio/
**Project Title**: Student Loan Default Risk Analysis – University of Chicago
**Author**: Urooj Abidi
**Email**: uroojabid203@gmail.com
**Date**: December 27, 2025
**Tool**: Python CLI Application
**License**: MIT (open-source portfolio project)

---

## 📋 Table of Contents
- [Objective](#-objective)
- [Scope](#-scope)
- [Input Data Specification](#-input-data-specification)
- [Output Requirements](#-output-requirements)
- [CLI Command Requirements](#-cli-command-requirements)
- [GitHub Repository Structure](#-github-repository-structure)
- [References](#-references)
- [Success Criteria](#-success-criteria)
- [Timeline](#-timeline-suggested)
- [Ethics & Compliance](#-ethics--compliance)

---

## 1. 🎯 Objective

To build an **accessible, transparent, and reproducible risk analysis CLI tool** that:
- Identifies key predictors of student loan default among University of Chicago-affiliated borrowers
- Provides actionable insights for financial counselors or institutional aid offices
- Demonstrates foundational data analysis skills using **Python programming**

> 🔍 **Note**: This is a **synthetic/simulated analysis** for educational purposes—**not real borrower data**.

---

## 2. 🧩 Scope

### ✅ In Scope
| Component | Description |
|--------|-------------|
| **Input Dataset** | CSV file with student loan records and relevant variables |
| **CLI Application** | Command-line interface for risk analysis |
| **Exploratory Data Analysis (EDA)** | Statistical summaries, correlations, risk factors |
| **Risk Segmentation** | Categorize loans into Low / Medium / High risk |
| **Summary Report** | CSV output with metrics and risk assessments |
| **GitHub Repository** | Public repo with data, Python code, and documentation |

### ❌ Out of Scope
- Real-time data integration
- Web deployment or dashboarding
- Use of actual student records (privacy-compliant by design)
- Machine learning model deployment

## 4. 🏗️ Architecture Diagram

View the system architecture diagram [here](../docs/diagram/architecture.mmd).

### 📊 System Components
- **Input Layer**: CSV data file containing loan records
- **Processing Layer**: Risk Analyzer CLI with validation and calculation modules
- **Output Layer**: Risk reports and analysis summaries
- **Error Handling**: Comprehensive error management throughout the process

---

## 5. 📊 Input Data Specification

| Field | Type | Description | Example |
|------|------|-----------|--------|
| `Loan_ID` | Text | Unique identifier | `UCH001` |
| `Age` | Integer | Borrower age at loan origination | `24` |
| `Citizenship` | Text | U.S. / International | `U.S.` |
| `Major` | Text | Field of study | `Economics` |
| `Degree_Level` | Text | Bachelor / Master / PhD / JD | `Bachelor` |
| `Expected_Income` | Integer | Projected post-grad income | `65000` |
| `Employment_Status` | Text | Employed / Unemployed | `Employed` |
| `Credit_Score` | Integer or N/A | Credit score (if available) | `720` |
| `Loan_Amount` | Integer | Loan principal amount | `30000` |
| `Interest_Rate` | Float | Annual interest rate (%) | `6.2` |
| `Monthly_Payment` | Integer | Estimated monthly payment | `335` |
| `DTI_Ratio` | Float | Debt-to-income ratio | `0.062` |
| `Has_Cosigner` | Text | Yes / No | `Yes` |
| `Default` | Text | Target variable: Yes / No | `No` |

> 📥 **File Format**: CSV file (UTF-8, comma-delimited)

---

## 6. 📈 Output Requirements

### A. **Risk Analysis Report** (CSV output)
Must include these sections:
1. `Summary_Stats` – Overall statistics and default rate
2. `Risk_Factors` – Analysis of key risk factors by category
3. `Individual_Assessments` – Risk scores for each loan
4. `Recommendations` – Actionable insights based on analysis

### B. **Calculated Fields (Python)**
| Field | Python Calculation |
|------|--------------------------|
| `Payment_to_Income_Ratio` | `Monthly_Payment / (Expected_Income / 12)` |
| `Risk_Score` | Weighted sum of risk factors |
| `Risk_Category` | Categorized based on Risk_Score thresholds |

---

## 7. 📋 CLI Command Requirements

### Command Syntax
```
python risk_analyzer.py --input <path_to_csv> --output <output_path>
```

### Command Options
- `--input`: Path to input CSV file (required)
- `--output`: Path for output CSV report (optional, defaults to risk_report.csv)
- `--verbose`: Enable detailed logging (optional)

### Expected Output
- CSV file with comprehensive risk analysis
- Console summary of key findings
- Risk scores and categories for each loan

### Testing
The application includes comprehensive unit tests to validate functionality:
```bash
python -m unittest discover tests/ -v
```

#### Test Categories
The test suite includes 19 tests across multiple categories:

**Risk Calculation Tests:**
- `test_calculate_risk_score_employed_low_income`: Test risk score calculation for employed person with low income
- `test_calculate_risk_score_unemployed`: Test risk score calculation for unemployed person
- `test_calculate_risk_score_high_dti`: Test risk score calculation for high DTI ratio
- `test_calculate_risk_score_low_credit`: Test risk score calculation for low credit score
- `test_calculate_risk_score_international`: Test risk score calculation for international student
- `test_calculate_risk_score_all_factors`: Test risk score calculation with all risk factors
- `test_assign_risk_category_low`: Test risk category assignment for low risk
- `test_assign_risk_category_medium`: Test risk category assignment for medium risk
- `test_assign_risk_category_high`: Test risk category assignment for high risk

**Risk Calculation Utility Tests:**
- `test_calculate_payment_to_income_ratio`: Test payment-to-income ratio calculation
- `test_calculate_payment_to_income_ratio_zero_income`: Test payment-to-income ratio with zero income

**Data Loading and Validation Tests:**
- `test_load_and_validate_data_success`: Test successful loading and validation of data
- `test_load_and_validate_data_missing_file`: Test error handling for missing file
- `test_load_and_validate_data_missing_columns`: Test error handling for missing required columns

**Analysis Function Tests:**
- `test_perform_analysis`: Test the perform_analysis function

**CLI Functionality Tests:**
- `test_main_function_calls`: Test that main function calls the right functions

**Integration Tests:**
- `test_load_real_csv_files`: Test loading all real CSV files
- `test_perform_analysis_on_real_data`: Test performing analysis on real data
- `test_risk_distribution_in_real_data`: Test risk distribution in real data

#### Test Coverage
Tests validate:
- CLI argument parsing
- CSV data validation and loading
- Risk calculation algorithms
- Risk category assignments
- Payment-to-income ratio calculations
- Output generation
- Error handling for missing files and invalid data
- Integration with real data files

---

## 8. 📁 GitHub Repository Structure

```
/uchicago-student-loan-risk/
├── README.md                 # Project overview, usage instructions
├── risk_analyzer.py          # Main Python CLI application
├── requirements.txt          # Python dependencies
├── data/
│   └── Qwen_csv_20251225_upsmabt6b.csv
├── output/
│   └── risk_report.csv       # Sample output file
└── docs/
    ├── PRD.md                # Product Requirements Document
    ├── technical_design_document.md # Technical Design Document
    ├── methodology.md        # EDA steps, assumptions, variable definitions
    └── references.md         # Citations (APA format)
```

> 📸 **README.md must include**:
> - Usage instructions for the CLI tool
> - Example output and findings
> - Link to public data sources (e.g., College Scorecard)
> - Note: “This is a synthetic educational project—no real borrower data used.”

---

## 9. 📚 References (APA Format)

Include in `docs/references.md`:

> U.S. Department of Education, Office of Federal Student Aid. (2023). *Federal student loan portfolio summary*. https://studentaid.gov/data-center/student/portfolio
>
> National Center for Education Statistics. (2022). *Student loan default rates by institution and completion status* (NCES 2022-155). https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2022155
>
> College Scorecard. (2025). *University of Chicago (172980)*. U.S. Department of Education. https://collegescorecard.ed.gov/school/?172980

---

## 10. ✅ Success Criteria

Your project is complete when:
- [ ] CLI application processes CSV input correctly
- [ ] Risk analysis report is generated in CSV format
- [ ] All key metrics are calculated accurately
- [ ] Risk scoring algorithm works as expected
- [ ] GitHub repo includes **README with usage instructions** and **proper citations**

---

## 11. ⏳ Timeline (Suggested)

| Task | Time Estimate |
|------|---------------|
| Update PRD for CLI approach | 0.5 hours |
| Design Python application | 1.5 hours |
| Implement CLI application | 2 hours |
| Test with sample data | 1 hour |
| Format GitHub repo + README | 1 hour |
| **Total** | **~6 hours** |

---

## 12. 🔐 Ethics & Compliance

- No real PII (personally identifiable information) used
- Synthetic data used for educational purposes only
- Clearly labeled as **synthetic educational project**
- Compliant with open-source software principles