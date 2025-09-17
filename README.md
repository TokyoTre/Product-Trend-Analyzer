## Overview

The **Product Trend Analyzer** is a Python project designed to analyze product sales data, detect trend candidates, rank suppliers, and recommend pricing strategies.  

This project demonstrates the **end-to-end pipeline for a retail AI workflow**, including:  
- Reading and validating sales data  
- Detecting trends in product sales  
- Ranking suppliers for products  
- Recommending pricing based on margins and sales data  

> **Note:** Current implementations use **stubbed values** for outputs. The code is fully functional and structured, ready for integration with real analytics logic.

---

## Table of Contents

1. [Project Structure](#project-structure)  
2. [Dependencies](#dependencies)  
3. [CSV Data Format](#csv-data-format)  
4. [Functions](#functions)  
5. [JSON Output](#json-output)  
6. [Usage](#usage)  
7. [Next Steps / Future Work](#next-steps--future-work)  

---

## Project Structure

product_trend_analyzer_project/
├── input_cases/
│ └── product_trend_analyzer_sales_data.csv
├── description.txt
├── test_cases.py
├── solution.py
├── revised-solution.txt
├── README.md
├── JSON-DEMO.txt
├── You_are_an_expert_AI_retail_an_results.json
└── pycache/

- **input_cases/** – Contains the CSV dataset.  
- **description.txt** – Project description and instructions.  
- **test_cases.py** – Contains test cases for the functions.  
- **solution.py** – Your main Python solution (stubs or functional).  
- **revised-solution.txt** – The revised/ upgraded version of your solution code.  
- **JSON-DEMO.txt** – Example output demonstrating function execution.  
- **You_are_an_expert_AI_retail_an_results.json** – Auto-generated JSON showing test results.  
- **__pycache__/** – Python cache directory.

## Dependencies

- Python 3.10+  
- pandas (if using dataframes, optional for stubs)  
- csv  
- json  

Install via pip:

```bash
pip install pandas
```

## CSV Data Format:

The project expects a CSV with the following columns:

Column        Type	      Description
product_id	  str	        Unique product identifier
sales_date	  date	      Date of sales
units_sold	  int        	Quantity sold
price	        float	      Unit price of product

Example:
product_id,sales_date,units_sold,price
prod_1,2025-01-01,10,20.0
prod_1,2025-01-02,15,20.0
prod_2,2025-01-01,5,30.0

## Files & Functions

### 1. `solution.py`

Contains the following stub functions:

#### `validate_schema(file_path: str) -> dict`

- Checks CSV has required columns.
- Example return:

```json
{
  "fatal": false,
  "errors": []
}
detect_trend_candidates(file_path: str, product_ids: list, threshold: int) -> list
Detects potential sales trends.

Current implementation returns stubs:
[
  {
    "product_id": "prod_1",
    "is_spike_candidate": false,
    "reason_tags": [],
    "velocity_pct_change_min": 0.0,
    "confidence_score_min": 0.0
  }
]
rank_suppliers_for_product(product_id: str, file_path: str) -> dict
Ranks suppliers for a product.

Example return:
{
  "product_id": "prod_1",
  "top_supplier": {
    "supplier_id": "sup_1",
    "rank_score_min": 0.0,
    "lead_time_days_max": 0
  }
}
recommend_pricing(product_id: str, target_margin_pct: float, base_price: float, file_path: str) -> dict
Suggests pricing strategies.

Example return:
{
  "product_id": "prod_1",
  "suggested_price_conservative_min": 0.0,
  "suggested_price_aggressive_max": 0.0,
  "target_margin_pct": 20.0
}
```
## JSON Demo Output:

- The **JSON-DEMO.txt** and **You_are_an_expert_AI_retail_an_results.json** files show example execution results.

- Each run includes:

```json
[
  {
    "function": "validate_schema",
    "input": ["input_cases/product_trend_analyzer_sales_data.csv"],
    "expected": {"fatal": false, "errors": []},
    "actual": {"fatal": false, "errors": []},
    "passed": true
  }
]
```
Demonstrates the pipeline execution, including trend detection, supplier ranking, and pricing stubs.

## Usage:

Run the analysis pipeline:

```bash
python solution.py
```
- Outputs are generated in JSON-DEMO.txt or You_are_an_expert_AI_retail_an_results.json.
- Demonstrates functionality without requiring full analytics implementation.

## Next Steps / Future Work:

- Replace stub values with **real analytics logic**:
  - Trend detection using moving averages, velocity, confidence scoring
  - Supplier ranking based on historical performance
  - Pricing recommendations based on cost, margin, and sales data
- Add visualizations or dashboards for trend reporting
- Optimize for large-scale data (e.g., 36,000+ products)

---

## Notes for Demonstration:

- Current implementation **shows the full pipeline execution**, even if values are placeholders.
- Perfect for showing:
  - CSV reading and validation
  - Structured output generation
  - Modular design with test cases
  - Easy-to-read JSON results



👤 Author
- Developed by Samuel A. Montgomery, III
- AI Developer & Prompt Engineer (Freelance-ready)
- Certifications: Generative AI Leader Professional Certificate (Google Cloud), IBM AI Developer Professional Certificate, Python for Data Science, AI & Development Certificate (IBM), Google AI Essentials Specialization, Google Prompting Essentials Specialization, Generative AI for Customer Support Specialization (IBM).