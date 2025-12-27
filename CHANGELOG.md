# Changelog
All notable changes to the Student Loan Default Risk Analysis project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Initial project structure for Student Loan Default Risk Analysis
- Product Requirements Document (PRD.md)
- Technical Design Document (technical_design_document.md)
- Test-Driven Development document (TDD.md)
- Qwen.md configuration file

## [1.0.0] - 2025-12-26
### Added
- Initial release of Student Loan Default Risk Analysis project
- Synthetic dataset with 50 student loan records (uchicago_loan_sample.csv)
- LibreOffice Calc analysis workbook (uchicago_risk_analysis.ods)
- Complete exploratory data analysis with PivotTables
- Risk segmentation and categorization system
- Summary report with key metrics and recommendations
- GitHub repository with proper documentation

### Changed
- Updated README.md with project overview, findings, and screenshots
- Implemented all calculated fields as specified in PRD:
  - Payment_to_Income_Ratio
  - Risk_Score
  - Risk_Category
- Created four PivotTables for analysis:
  - Default rate by Graduated
  - Default rate by Major
  - Avg. income by Default
  - Default rate by Loan Type
- Added three visualization charts:
  - Bar chart: Default % by Major
  - Scatter: Income vs Monthly Payment (color by Default)
  - Pie: Loan Type Distribution

### Fixed
- Ensured all formulas are properly documented
- Validated dataset contains exactly 50 rows as required
- Confirmed all data types match PRD specifications

## [0.1.0] - 2025-12-26
### Added
- Project initialization with basic structure
- Product Requirements Document outlining project scope
- Data schema definition for student loan records
- Initial documentation files