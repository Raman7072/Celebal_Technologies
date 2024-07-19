# Weekly assignments of Celebel COE Week-7

# Azure Components Used: Azure Data Lake Storage Gen2:

Use Azure Data Lake Storage Gen2 as the storage repository for your files (data lake container in your case). Azure Databricks:

Utilize Azure Databricks for scalable data processing. It provides an Apache Spark-based analytics platform with built-in integration to Azure services. Azure SQL Database:

Use Azure SQL Database to store your structured data (CUST_MSTR, master_child, H_ECOM_Orders tables). Azure Data Factory:

Orchestrate and automate data movement and transformation using Azure Data Factory. Steps to Implement:

Set Up Azure Data Lake Storage Gen2 Create an Azure Data Lake Storage Gen2 account. Upload your files (CUST_MSTR_.csv, master_child_export-.csv, H_ECOM_ORDER.csv) into containers within this storage account. Set Up Azure SQL Database Create Azure SQL Database instances for CUST_MSTR, master_child, and H_ECOM_Orders tables. Define the schema for each table to match your data requirements. Use Azure Data Factory for Orchestration Create Linked Services: Configure linked services for Azure Data Lake Storage Gen2 and Azure SQL Database within Azure Data Factory. Define Datasets:

Create datasets in Azure Data Factory for each type of file (CUST_MSTR, master_child_export, H_ECOM_ORDER). Define the file format and schema in the datasets. Create Pipelines:

Create separate pipelines in Azure Data Factory for each type of file processing. Pipeline Steps:

For CUST_MSTR Files:

Use a Copy activity to load files starting with "CUST_MSTR". Use Data Flow activity (Azure Data Factory Mapping Data Flows) to transform the data: Extract date from filename and format it as "YYYY-MM-DD". Add a new column "Date". Use SQL Server Sink to write data to CUST_MSTR table in Azure SQL Database. For master_child_export Files:

Similar to CUST_MSTR files, use Copy activity to load files starting with "master_child_export". Use Data Flow activity to transform the data: Extract date from filename and format it as "YYYY-MM-DD" for "Date" column. Extract date and format it as "YYYYMMDD" for "DateKey" column. Use SQL Server Sink to write data to master_child table. For H_ECOM_ORDER Files:

Directly load these files into Azure SQL Database using Copy activity, as they do not require transformation. 4. Automate with Triggers Set up triggers in Azure Data Factory to run these pipelines on a daily basis. Triggers can be scheduled triggers (e.g., run daily at a specific time) or event-based triggers (e.g., run when new files are added to the data lake container). 5. Monitoring and Error Handling Monitor pipeline runs and data loads in Azure Data Factory Monitoring. Implement error handling mechanisms (e.g., retry logic, logging) within Azure Data Factory pipelines.
