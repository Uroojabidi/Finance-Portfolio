# 📊 Student Loan Default Risk Analysis – University of Chicago

**Project Title**: Student Loan Default Risk Analysis – University of Chicago
**Author**: Urooj Abidi
**Date**: December 26, 2025
**Tool**: LibreOffice Calc (v7.6+)
**License**: MIT (open-source portfolio project)

---

## 🎯 Project Overview

This project implements an **accessible, transparent, and reproducible risk analysis workbook** that:
- Identifies key predictors of student loan default among University of Chicago-affiliated borrowers
- Provides actionable insights for financial counselors or institutional aid offices
- Demonstrates foundational data analysis skills using **only spreadsheet tools** (no coding)

> 🔍 **Note**: This is a **synthetic/simulated analysis** for educational purposes—**not real borrower data**.

---

## 📁 Repository Structure

```
/uchicago-student-loan-risk/
├── README.md                 # Project overview, findings, screenshots
├── CHANGELOG.md              # Version history and changes
├── COMMIT_MESSAGES.md        # Suggested commit messages
├── data/
│   └── uchicago_loan_sample.csv
├── analysis/
│   └── uchicago_risk_analysis.ods   # LibreOffice Calc file
└── docs/
    ├── PRD.md                # Product Requirements Document
    ├── TDD.md                # Test-Driven Development Document
    ├── technical_design_document.md # Technical Design Document
    ├── methodology.md        # EDA steps, assumptions, variable definitions
    └── references.md         # Citations (APA format)
```

---

## 📊 Analysis Findings

### 📌 Executive Summary
> "In this synthetic sample of 50 University of Chicago-affiliated borrowers, 18% defaulted. Non-graduates, private loan holders, and borrowers with expected income below $45K are at highest risk."

### 📊 Key Metrics Table
| Metric | Value |
|------|-------|
| Total Loans | 50 |
| Default Rate | 18% |
| Avg. Income (Default) | $36,200 |
| Avg. Income (Paid) | $82,500 |
| Default Rate (Not Graduated) | 67% |

### 🛡️ Recommendations
1. Prioritize **degree completion support** for at-risk students
2. Counsel private loan borrowers on **federal consolidation**
3. Flag majors with **low ROI** for financial literacy programs

---

## 📈 Analysis Components

### PivotTables
1. **Default rate by Graduated** - Shows the relationship between degree completion and loan default
2. **Default rate by Major** - Identifies fields of study with higher default rates
3. **Avg. income by Default** - Compares income levels between defaulted and repaid loans
4. **Default rate by Loan Type** - Analyzes differences between federal and private loans

### Charts
1. **Bar chart: Default % by Major** - Visualizes default rates across different fields of study
2. **Scatter: Income vs Monthly Payment** - Shows the relationship between income and payment burden, color-coded by default status
3. **Pie: Loan Type Distribution** - Displays the proportion of federal vs private loans in the sample

### Calculated Fields
1. **Payment_to_Income_Ratio** - `=Monthly_Payment / (Expected_Annual_Income / 12)`
2. **Risk_Score** - `=IF(Graduated="No",2,0) + IF(Loan_Type="Private",3,0) + IF(Expected_Annual_Income<45000,2,0)`
3. **Risk_Category** - `=IF(Risk_Score>=5,"High",IF(Risk_Score>=2,"Medium","Low"))`

---

## 🖼️ Screenshots

> [Screenshots of key charts and tables would be inserted here once the LibreOffice Calc file is created]
>
> 1. PivotTable showing default rates by graduation status
> 2. Bar chart visualizing default rates by major
> 3. Scatter plot showing income vs monthly payment relationship

---

## 🚀 Getting Started

### Prerequisites
- LibreOffice Calc (v7.6+) or compatible spreadsheet software
- Basic knowledge of spreadsheet functions and PivotTables

### Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/uchicago-student-loan-risk.git
   ```

2. Open `analysis/uchicago_risk_analysis.ods` in LibreOffice Calc

3. Navigate through the different sheets:
   - `Raw_Data` - Cleaned input dataset
   - `PivotTables` - Various analytical breakdowns
   - `Charts` - Visual representations of the data
   - `Summary_Report` - Executive summary and recommendations

---

## 📚 References (APA Format)

> U.S. Department of Education, Office of Federal Student Aid. (2023). *Federal student loan portfolio summary*. https://studentaid.gov/data-center/student/portfolio

> National Center for Education Statistics. (2022). *Student loan default rates by institution and completion status* (NCES 2022-155). https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2022155

> College Scorecard. (2025). *University of Chicago (172980)*. U.S. Department of Education. https://collegescorecard.ed.gov/school/?172980

---

## 🤝 Contributing

This is an educational project for portfolio purposes. If you'd like to contribute or suggest improvements, please open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Ethics & Compliance

- No real PII (personally identifiable information) used
- Race/gender used **only for disparity analysis**, not prediction
- Clearly labeled as **synthetic educational project**
- Compliant with LibreOffice's open-source ethos
