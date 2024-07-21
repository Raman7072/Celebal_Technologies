# Here's a detailed breakdown of the required components and their approximate costs:

## 1. Azure Data Factory (ADF)
ADF will orchestrate the data movement and transformation from the three data sources to the Azure SQL Database.

Pipelines and Activities: We need ADF pipelines to handle the extraction, transformation, and loading (ETL) processes.
Data Movement: We need Integration Runtimes for data transfer, especially for the on-premise Oracle database.

## 2. Azure Integration Runtime
For the data movement from the on-premise Oracle database, we need a self-hosted integration runtime.

## 3. Azure SQL Database
A SQL Database to store the processed data. Given the volume, we might opt for a Business Critical tier to ensure performance and reliability.

## 4. Azure Data Lake Storage Gen2
To store the intermediate and semi-structured data coming from FTP.

## 5. Data Transfer Costs
Cost associated with moving data into Azure, particularly from the on-premise Oracle database.

# Step-by-Step Cost Calculation
## Azure Data Factory
Pipeline Activity Runs: Estimate the number of activities and pipeline runs per month.
Data Movement: Cost of moving data from Oracle, Salesforce, and FTP.

## Azure Integration Runtime
Self-Hosted IR: For moving data from Oracle to Azure.

## Azure SQL Database
Business Critical Tier: To handle the expected volume and ensure high performance.

## Azure Data Lake Storage Gen2
Storage Costs: For storing semi-structured files.
Operations Costs: For read/write operations.

## Data Transfer
Inbound Data Transfer: From Oracle and FTP.

# Estimating Costs
## Azure Data Factory
Pipeline and Activity Runs: Estimate 50,000 activity runs per month.
Data Movement: 30 GB from Oracle, 50 GB from Salesforce, and 5 GB from FTP.

## Azure Integration Runtime
Self-Hosted IR: Assumed to be always on.

## Azure SQL Database
Business Critical Tier: Estimate for a database capable of handling the total data volume.

## Azure Data Lake Storage Gen2
Storage: 60 GB/month.
Operations: Estimate 100,000 operations per month.

# Example Cost Calculation (using Azure Pricing Calculator)
## 1. Azure Data Factory:
### Activity runs: $0.00025 per activity run × 50,000 = _$12.50_
### Data movement: $0.25 per GB × 85 GB = _$21.25_

## 2. Azure Integration Runtime:
### Self-hosted IR: $0.10 per hour × 24 hours × 30 days = _$72.00_

## 3. Azure SQL Database:
### Business Critical (vCore): Estimated at _$750_ per month

## 4. Azure Data Lake Storage Gen2:
### Storage: $0.0184 per GB × 60 GB = _$1.10_
### Operations: $0.0004 per 10,000 transactions × 100,000 = _$0.04_

## 5. Data Transfer:
### Inbound Data Transfer: Typically free within Azure, but ensure no hidden costs.

# Total Estimated Monthly Cost
Azure Data Factory: **_$33.75_**
Azure Integration Runtime: **_$72.00_**
Azure SQL Database: **_$750.00_**
Azure Data Lake Storage Gen2: **_$1.14_**
Data Transfer: **_$0.00_**
### Total: $856.89 per month
