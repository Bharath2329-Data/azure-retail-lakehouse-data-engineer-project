# 🚀 Azure Retail Lakehouse Project (End-to-End Data Engineering)

## 📌 Project Overview

This project demonstrates the design and implementation of an **end-to-end Azure Data Engineering pipeline** using modern cloud technologies.

The solution follows the **Medallion Architecture (Bronze → Silver → Gold)** to ingest, transform, validate, and analyze retail data.

This project was built in **10 days** with a focus on **real-world data engineering practices, cost optimization, and CI/CD automation**.

---

## 🎯 Project Objective

- Build a scalable Azure-based data pipeline  
- Implement Bronze, Silver, and Gold layers  
- Perform data transformation using PySpark  
- Generate business insights using SQL  
- Apply data quality checks  
- Integrate CI/CD using GitHub Actions  
- Maintain a low-cost cloud architecture  

---

## 🏗 Architecture Overview

Retail CSV Files
↓
Azure Data Factory (Ingestion)
↓
ADLS Gen2 Bronze Layer (Raw Data)
↓
Azure Databricks (PySpark Transformations)
↓
ADLS Gen2 Silver Layer (Delta Tables)
↓
Azure Databricks (Aggregations)
↓
ADLS Gen2 Gold Layer (Analytics Tables)
↓
SQL Analytics / Reporting


---

## 🧰 Technology Stack

- Azure Data Lake Storage Gen2 (ADLS)
- Azure Data Factory (ADF)
- Azure Databricks
- PySpark
- Delta Lake
- SQL (Spark SQL)
- GitHub
- GitHub Actions (CI/CD)
- PowerShell

---

## 📂 Dataset Description

The project uses simulated retail datasets:

- customers  
- products  
- stores  
- orders  
- order_items  
- payments  

These datasets support analytics such as:

- revenue trends  
- product performance  
- customer lifetime value  

---

## 🪜 Medallion Architecture

### 🔹 Bronze Layer
- Raw CSV data stored in ADLS  
- No transformation applied  
- Immutable storage  

### 🔹 Silver Layer
- Cleaned and standardized data  
- Data type conversions  
- Duplicate removal  
- Added audit columns (`ingest_ts`)  
- Stored as Delta tables  

### 🔹 Gold Layer
- Business-ready analytics tables  
- Aggregated metrics  
- Optimized for reporting  

---

## 📅 Day-by-Day Implementation

| Day | Task | Outcome |
|-----|------|--------|
| Day 1 | Project setup | Azure resources + repo structure |
| Day 2 | Data ingestion | Retail CSV datasets uploaded to Bronze |
| Day 3 | ADF setup | Linked service + datasets |
| Day 4 | Pipeline | Parameterized ingestion pipeline |
| Day 5 | Silver layer | Data cleaning using PySpark |
| Day 6 | Gold layer | Business analytics tables |
| Day 7 | Data quality | Validation checks implemented |
| Day 8 | CI/CD | GitHub Actions workflow |
| Day 9 | Documentation | Runbook, architecture, cost guide |
| Day 10 | Final polish | LinkedIn-ready project |
