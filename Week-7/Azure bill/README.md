# Here's a detailed breakdown of the required components and their approximate costs:

## 1. Azure Data Factory (ADF)
ADF will orchestrate the data movement and transformation from the three data sources to the Azure SQL Database.

Pipelines and Activities: We need ADF pipelines to handle the extraction, transformation, and loading (ETL) processes.
Data Movement: We need Integration Runtimes for data transfer, especially for the on-premise Oracle database.

## 2. Azure Integration Runtime
For the data movement from the on-premise Oracle database, we need a self-hosted integration runtime.

## 3. Azure SQL Database
A SQL Database to store the processed data. Given the volume, we might opt for a Business Critical tier to ensure performance and reliability.
