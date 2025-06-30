import pandas as pd

# Load the dataset
data_path = "C:/Users/su_te/Documents/olist-ecommerce-project/data/olist_customers_dataset.csv"
data = pd.read_csv(data_path)

# Display the first few rows
print("First few rows of the data:")
print(data.head())

# Data summary (info)
print("\nData summary (info):")
print(data.info())

# Check for duplicates
print("\nChecking for duplicates:")
print(f"Number of duplicate rows: {data.duplicated().sum()}")

# Remove duplicate rows (if any)
data_cleaned = data.drop_duplicates()

# Check for missing values
print("\nChecking for missing values:")
print(data_cleaned.isnull().sum())

# Optional: Standardize city and state column (capitalize first letter)
data_cleaned['customer_city'] = data_cleaned['customer_city'].str.title()
data_cleaned['customer_state'] = data_cleaned['customer_state'].str.upper()

# Save cleaned data to a new CSV file
cleaned_data_path = "C:/Users/su_te/Documents/olist-ecommerce-project/data/olist_customers_cleaned.csv"
data_cleaned.to_csv(cleaned_data_path, index=False)

# Display the first few rows of the cleaned data
print("\nCleaned data (first few rows):")
print(data_cleaned.head())

# Display data summary of cleaned data
print("\nCleaned data summary (info):")
print(data_cleaned.info())

print(f"\nCleaned data saved to: {cleaned_data_path}")