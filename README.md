# Azure Retail Lakehouse Project

## Objective
Build an end-to-end retail analytics lakehouse using Azure cloud services.

## Architecture
- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- Bronze / Silver / Gold architecture (Medallion Architecture)

## Status
## Day 1: Environment setup complete
## Objective

Establish a secure, cost-optimized Azure foundation for building a scalable Retail Lakehouse architecture.

 Azure Resources Created

Resource Group: rg-retail-lakehouse-dev

Storage Account: retaillakehousebharath

Storage Type: Azure Data Lake Storage Gen2

Performance Tier: Standard

Redundancy: LRS (Locally Redundant Storage) – cost optimized

Hierarchical Namespace: Enabled (required for ADLS Gen2)

## Data Lake Structure (Medallion Architecture)

Created the following containers:

bronze → Raw data layer

silver → Cleaned & transformed data layer

gold → Business-ready analytics layer

logs → Pipeline and operational logs

This structure enables scalable and modular data processing following industry-standard lakehouse patterns.

## Cost Optimization Strategy

To ensure the project stays under a $20 budget:

Selected LRS redundancy (cheapest option)

Used Standard performance tier

Consolidated all resources inside a single Resource Group

Designed for easy teardown using:

az group delete --name rg-retail-lakehouse-dev

This ensures full environment cleanup to prevent unexpected charges.

## Security & Governance (Foundation)

Storage account secured via Azure RBAC

Public access disabled where possible

Designed to integrate with Managed Identity and Key Vault in future phases

## Git Version Control

Initialized Git repository

Created structured project folders

Added initial README and documentation skeleton

Committed environment setup changes


## Day 2 — Retail Data Ingestion (Bronze Layer)

Create realistic retail datasets and upload them into the Azure Data Lake Bronze layer as raw source data.

## Architecture (Current State)

Retail CSV Files
⬇
Azure Data Lake Storage Gen2
⬇
Bronze Layer (Raw Data)

📂 Datasets Created

The following retail datasets were generated:

## Dataset	Description
customers	Customer master data with loyalty tier
products	Product catalog with categories and pricing
stores	Store location details
orders	Order header information
order_items	Line-level product transactions
payments	Payment details per order

All datasets are stored locally under:

data/sample_raw/
## ☁ Bronze Layer Structure (ADLS)

Uploaded to Azure Data Lake:

bronze/raw/customers/
bronze/raw/products/
bronze/raw/stores/
bronze/raw/orders/
bronze/raw/order_items/
bronze/raw/payments/
Bronze Layer Rules

Raw data only

No transformations

No schema enforcement

Immutable storage

 ## Data Validation Performed

Using Databricks:

Loaded CSV files from Bronze

Verified schema structure

Checked row counts

Validated relational integrity between:

orders and order_items

orders and payments

Performed null checks

This ensures source data quality before transformation.

🛠 Technologies Used

Azure Data Lake Storage Gen2

Azure Portal

Databricks (PySpark)

GitHub

PowerShell (Git version control)


