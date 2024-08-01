# Task 01
## 1: Load the Customer Dataset
```
import pandas as pd
```
#Load customer dataset
```
customer_data = pd.read_csv('customers.csv')
print(customer_data.head())
```

## 2: Identify Duplicate Customers
#Mark duplicate customers based on Name and Address
```
customer_data['is_duplicate'] = customer_data.duplicated(subset=['Name', 'Address'], keep=False)
print(customer_data.head())
```
