# 📄 Product Requirements Document (PRD)  
**Project Title**: Student Loan Default Risk Analysis – University of Chicago  
**Author**: Urooj Abidi 
**Date**: December 27, 2025  
**Tool**: LibreOffice Calc (v7.6+)  
**License**: MIT (open-source portfolio project)  

---

## 1. 🎯 Objective

To build an **accessible, transparent, and reproducible risk analysis workbook** that:
- Identifies key predictors of student loan default among University of Chicago-affiliated borrowers
- Provides actionable insights for financial counselors or institutional aid offices
- Demonstrates foundational data analysis skills using **only spreadsheet tools** (no coding)

> 🔍 **Note**: This is a **synthetic/simulated analysis** for educational purposes—**not real borrower data**.

---

## 2. 🧩 Scope

### ✅ In Scope
| Component | Description |
|--------|-------------|
| **Input Dataset** | Synthetic sample of 50 student loan records with UChicago-relevant variables |
| **Exploratory Data Analysis (EDA)** | PivotTables, histograms, conditional formatting, calculated fields |
| **Risk Segmentation** | Categorize loans into Low / Medium / High risk |
| **Summary Report** | One-page executive summary with metrics and recommendations |
| **GitHub Repository** | Public repo with data, analysis file, and documentation |

### ❌ Out of Scope
- Real-time data integration
- Machine learning or statistical modeling
- Web deployment or dashboarding
- Use of actual student records (privacy-compliant by design)

---

## 3. 📊 Input Data Specification

| Field | Type | Description | Example |
|------|------|-----------|--------|
| `Loan_ID` | Text | Unique identifier | `S001` |
| `Student_ID` | Text | Anonymized student ID | `UCHI001` |
| `Age` | Integer | Borrower age at loan origination | `24` |
| `Gender` | Text | Male / Female / Non-Binary | `Female` |
| `Race_Ethnicity` | Text | U.S. federal categories (for equity analysis only) | `Black` |
| `Major` | Text | Field of study | `Economics` |
| `Graduated` | Boolean | Yes / No | `Yes` |
| `Disability` | Boolean | Yes / No | `No` |
| `Military` | Boolean | Yes / No | `No` |
| `Employment_Status` | Text | Unemployed / Part-Time / Full-Time | `Full-Time` |
| `Expected_Annual_Income` | Currency | Projected post-grad income | `85000` |
| `Loan_Type` | Text | Federal / Private | `Federal` |
| `Principal_Balance` | Currency | Initial loan amount | `32000` |
| `Interest_Rate` | Percentage | Annual rate (%) | `5.05` |
| `Monthly_Payment` | Currency | Estimated payment | `340` |
| `Repayment_Plan` | Text | Standard / Income-Driven | `Standard` |
| `Default` | Boolean | Target variable: Yes / No | `No` |

> 📥 **File Format**: `data/uchicago_loan_sample.csv` (UTF-8, comma-delimited)

---

## 4. 📈 Output Requirements

### A. **Analysis Workbook** (`analysis/uchicago_risk_analysis.ods`)
Must include these sheets:
1. `Raw_Data` – Cleaned input dataset  
2. `PivotTables` –  
   - Default rate by `Graduated`  
   - Default rate by `Major`  
   - Avg. income by `Default`  
   - Default rate by `Loan_Type`  
3. `Charts` –  
   - Bar chart: Default % by Major  
   - Scatter: Income vs Monthly Payment (color by Default)  
   - Pie: Loan Type Distribution  
4. `Summary_Report` – Executive summary (as described in Section 5)

### B. **Calculated Fields (Formulas)**
| Field | LibreOffice Calc Formula |
|------|--------------------------|
| `Payment_to_Income_Ratio` | `=Monthly_Payment / (Expected_Annual_Income / 12)` |
| `Risk_Score` | `=IF(Graduated="No",2,0) + IF(Loan_Type="Private",3,0) + IF(Expected_Annual_Income<45000,2,0)` |
| `Risk_Category` | `=IF(Risk_Score>=5,"High",IF(Risk_Score>=2,"Medium","Low"))` |

> 💡 **Note**: All formulas must be **documented in comments** or a `Formulas` sheet.

---

## 5. 📋 Summary Report Content

Include on a dedicated sheet in the ODS file:

### 📌 Executive Summary
> “In this synthetic sample of 50 University of Chicago-affiliated borrowers, 18% defaulted. Non-graduates, private loan holders, and borrowers with expected income below $45K are at highest risk.”

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

## 6. 📁 GitHub Repository Structure

```
/uchicago-student-loan-risk/
├── README.md                 # Project overview, findings, screenshots
├── data/
│   └── uchicago_loan_sample.csv
├── analysis/
│   └── uchicago_risk_analysis.ods   # LibreOffice Calc file
└── docs/
    ├── methodology.md        # EDA steps, assumptions, variable definitions
    └── references.md         # Citations (APA format)
```

> 📸 **README.md must include**:  
> - 2–3 screenshots of key charts/tables  
> - Link to public data sources (e.g., College Scorecard)  
> - Note: “This is a synthetic educational project—no real borrower data used.”

---

## 7. 📚 References (APA Format)

Include in `docs/references.md`:

> U.S. Department of Education, Office of Federal Student Aid. (2023). *Federal student loan portfolio summary*. https://studentaid.gov/data-center/student/portfolio  
>  
> National Center for Education Statistics. (2022). *Student loan default rates by institution and completion status* (NCES 2022-155). https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2022155  
>  
> College Scorecard. (2025). *University of Chicago (172980)*. U.S. Department of Education. https://collegescorecard.ed.gov/school/?172980

---

## 8. ✅ Success Criteria

Your project is complete when:
- [ ] Dataset has **exactly 50 rows**, matches spec
- [ ] LibreOffice file opens without errors
- [ ] All PivotTables and charts are **dynamic** (refreshable)
- [ ] Summary report fits on **one page**
- [ ] GitHub repo includes **README with screenshots** and **proper citations**

---

## 9. ⏳ Timeline (Suggested)

| Task | Time Estimate |
|------|---------------|
| Build dataset & import into Calc | 1 hour |
| Create PivotTables & charts | 2 hours |
| Write summary & formulas | 1 hour |
| Format GitHub repo + README | 1 hour |
| **Total** | **~5 hours** |

---

## 10. 🔐 Ethics & Compliance

- No real PII (personally identifiable information) used  
- Race/gender used **only for disparity analysis**, not prediction  
- Clearly labeled as **synthetic educational project**  
- Compliant with LibreOffice’s open-source ethos  
s