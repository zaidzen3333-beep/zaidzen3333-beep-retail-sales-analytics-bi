# Global Retail Sales & Store Optimization Analytics

End-to-end data analytics and Business Intelligence project transforming 62,884 retail transactions (2016–2021) into executive recommendations for revenue growth, SKU rationalization, and store footprint optimization.

## Tech Stack
- **Python**: `pandas`, `numpy`, `matplotlib`, `seaborn` (Data Audit, ETL Pipeline, Validation, & Business Analysis)
- **SQL (PostgreSQL)**: Star Schema DDL (`dim_*`, `fact_sales`) and analytical views
- **Power BI**: Dimensional Star Schema data model, DAX measures, and 3-page interactive executive dashboard

## Project Structure
├── data/
│   ├── raw/                  # Original source CSVs
│   └── processed/            # Cleaned tables & sales_master_analytical.csv
├── docs/
│   ├── client_brief.md       # Business questions & project scope
│   ├── Data_Dictionary.md    # Schema & field definitions
│   └── final_report.md       # Executive summary & recommendations
├── notebooks/
│   ├── 01_data-audit.ipynb
│   ├── 02_cleaning_and_eda.ipynb
│   └── 03_business_analysis.ipynb
├── sql/
│   ├── 01_schema_star_model.sql
│   ├── 02_load_data.sql
│   └── 03_create_views.sql
├── src/
│   ├── clean_data.py         # Automated ETL pipeline
│   └── validate_data.py      # Data quality & integrity assertions
└── dashboard/
    ├── retail_sales_analytics.pbix
    ├── README.md             # Data model & DAX documentation
    └── screenshots/          # Dashboard page previews

## Key Findings
- **Overall Performance**: **$55.76M** total revenue, **$32.66M** gross profit (**58.6%** gross margin) across **~26K** orders (79.5% In-Store vs. 20.5% Online).
- **Revenue Concentration (Pareto)**: **28.4%** of products (708 of 2,492 SKUs) generate **80%** of total revenue, led by **Computers ($19.3M)**.
- **Underperforming SKUs**: **805 SKUs (32.3%)** sit in the low-revenue/low-volume quadrant, representing immediate markdown or delisting candidates.
- **Store Footprint Efficiency**: Compact **800–1,200 sqm** stores consistently outperform **2,000+ sqm** locations in sales density—led by **Store 66 (Wyoming)** at **$1,453.53/sqm**.
- **Trend & Seasonality**: Revenue peaked in 2019 (**$18.3M**) before a **49.2%** drop in 2020 (**$9.3M**) driven by physical retail disruptions (2021 data covers Jan 1 – Feb 20).
- **Customer Dynamics**: Customers aged **35–64** drive **~65%** of revenue, with a **55.4%** repeat purchase rate.

## Dashboard Previews
### 1. Executive Overview
[dashboard/screenshots/01_executive_overview.png]

### 2. Product & Category Analysis
[dashboard/screenshots/02_product_analysis.png]

### 3. Store & Footprint Optimization
[dashboard/screenshots/03_store_optimization.png]

## How to Run
1. Run the automated cleaning & validation pipeline:
   ```bash
   python src/clean_data.py
   python src/validate_data.py