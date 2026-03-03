# Azure Retail Lakehouse Project

## Objective
Build an end-to-end retail analytics lakehouse using Azure cloud services.

## Architecture
- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- Bronze / Silver / Gold architecture (Medallion Architecture)

## Status
# Day 1: Environment setup complete
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

### Cost Optimization Strategy

To ensure the project stays under a $20 budget:

Selected LRS redundancy (cheapest option)

Used Standard performance tier

Consolidated all resources inside a single Resource Group

Designed for easy teardown using:

az group delete --name rg-retail-lakehouse-dev

This ensures full environment cleanup to prevent unexpected charges.

### Security & Governance (Foundation)

Storage account secured via Azure RBAC

Public access disabled where possible

Designed to integrate with Managed Identity and Key Vault in future phases

### Git Version Control

Initialized Git repository

Created structured project folders

Added initial README and documentation skeleton

Committed environment setup changes


# Day 2 — Retail Data Ingestion (Bronze Layer)

Create realistic retail datasets and upload them into the Azure Data Lake Bronze layer as raw source data.

## Architecture (Current State)

Retail CSV Files
⬇
Azure Data Lake Storage Gen2
⬇
Bronze Layer (Raw Data)

📂 Datasets Created

The following retail datasets were generated:

### Dataset	Description
customers	Customer master data with loyalty tier
products	Product catalog with categories and pricing
stores	Store location details
orders	Order header information
order_items	Line-level product transactions
payments	Payment details per order

All datasets are stored locally under:

data/sample_raw/
###  Bronze Layer Structure (ADLS)

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

# Day 3 — Azure Data Factory Setup & Bronze Integration
## Goal

Establish Azure Data Factory (ADF) to orchestrate data ingestion from Azure Data Lake Storage Gen2 (ADLS) Bronze layer.

This step introduces orchestration and enterprise-grade data pipeline design.

### Architecture (Updated)

Retail CSV Files
⬇
Azure Data Lake (Bronze Layer)
⬇
Azure Data Factory (Orchestration Layer)

### Azure Resources Created
1️⃣ Azure Data Factory (V2)

Name: adf-retail-lakehouse

Resource Group: rg-retail-lakehouse-bharath

Region: Same as ADLS

System Assigned Managed Identity: Enabled

### Role-Based Access Control (RBAC)

To allow ADF to access ADLS securely:

Assigned Role: Storage Blob Data Contributor

Assigned To: Azure Data Factory Managed Identity

This enables secure, password-less authentication using Azure RBAC.

### Linked Service Configuration

Created Linked Service:

Name: LS_ADLS_RETAIL

Type: Azure Data Lake Storage Gen2

Authentication: Managed Identity

Connection Test: Successful

This establishes secure connectivity between ADF and ADLS.

### Datasets Created (Bronze Layer)

The following datasets were configured in ADF:

Dataset Name	Source Path
DS_Bronze_Customers_CSV	bronze/raw/customers/customers.csv
DS_Bronze_Products_CSV	bronze/raw/products/products.csv
DS_Bronze_Stores_CSV	bronze/raw/stores/stores.csv
DS_Bronze_Orders_CSV	bronze/raw/orders/orders.csv
DS_Bronze_OrderItems_CSV	bronze/raw/order_items/order_items.csv
DS_Bronze_Payments_CSV	bronze/raw/payments/payments.csv

Each dataset:

Uses DelimitedText format

Reads from ADLS Gen2

Schema imported from source

Header row enabled

 What This Demonstrates

✔ Azure Data Factory configuration
✔ Managed Identity authentication
✔ Secure RBAC role assignment
✔ Enterprise data connectivity
✔ Dataset design for structured ingestion

This step transitions the project from static storage to orchestrated data engineering.

### ADF Configuration Exported

ADF ARM Template exported and stored in repository:

adf/arm_template/
  ARMTemplateForFactory.json
  ARMTemplateParametersForFactory.json

This enables Infrastructure-as-Code capability and reproducibility.




