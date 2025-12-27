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
- Comprehensive test specifications in PRD and Technical Design Document
- "Buy Me A Coffee" and Indeed profile links in README

### Changed
- Enhanced PRD with detailed test cases covering all functionality
- Updated Technical Design Document with comprehensive testing strategy
- Improved CLI command documentation in PRD
- Added detailed test execution instructions
- Organized tests into logical categories (Risk Calculation, Data Validation, etc.)

## [2.0.0] - 2025-12-26
### Added
- Complete Python CLI application for risk analysis (risk_analyzer.py)
- Unit tests using real CSV data as test fixtures
- Comprehensive testing framework with pytest support
- Risk scoring algorithm with multiple weighted factors
- CLI argument parsing with input/output options
- Detailed CSV output with multiple analysis sections

### Changed
- Migrated from LibreOffice Calc to Python CLI application
- Updated PRD to reflect CLI-based approach
- Updated README with CLI usage and testing instructions
- Enhanced risk analysis algorithm with 6 weighted factors
- Improved output format with structured CSV report

### Fixed
- Implemented proper error handling for CSV validation
- Added comprehensive data validation checks
- Enhanced risk calculation accuracy

## [1.0.0] - 2025-12-26
### Added
- Initial release of Student Loan Default Risk Analysis project
- Synthetic dataset with 50 student loan records (uchicago_loan_sample.csv)
- LibreOffice Calc analysis workbook (uchicago_risk_analysis.ods_structure.txt)
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