## 1. Set Up Unity Catalog Metastore in an Azure Databricks Environment
### 1.1. Prerequisites:
- Ensure you have access to an Azure subscription and a Databricks workspace.
- Ensure you have the necessary Azure roles (`Owner` or `Contributor`) to create and manage resources.
- Databricks Premium Plan is required for Unity Catalog.

## 2. Create the Root Storage Account for the Metastore
### 2.1. Create an Azure Storage Account:
    1. Go to the `Azure portal` and select Storage accounts.
    2. Click on + **Create** and configure the following:
        - **Subscription:** Choose your subscription.
        - **Resource group:** Create a new resource group or use an existing one.
        - **Storage account name:** Enter a unique name for the storage account.
        - **Region:** Select the region that matches your Databricks workspace.
        - **Performance:** Standard.
        - **Redundancy:** Locally-redundant storage (LRS) is sufficient.
