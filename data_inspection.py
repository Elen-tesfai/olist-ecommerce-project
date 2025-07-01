import pandas as pd

# Path to your raw dataset
data_path = "C:/Users/su_te/Documents/olist-ecommerce-project/data/olist_customers_dataset.csv"

# Load CSV with proper quoting to handle quotes in header and data
data = pd.read_csv(
    data_path,
    encoding='utf-8',
    quotechar='"',
    delimiter=',',
    engine='python',
    on_bad_lines='skip'  # skip malformed lines
)

# Strip quotes from column names if any remain
data.columns = data.columns.str.strip('"')

print("Columns after fixing headers:")
print(data.columns.tolist())

# Strip whitespace and quotes from string columns
for col in ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']:
    if col in data.columns:
        # Convert to string, strip whitespace and quotes
        data[col] = data[col].astype(str).str.strip().str.strip('"')

# Standardize city and state formatting
data['customer_city'] = data['customer_city'].str.title()
data['customer_state'] = data['customer_state'].str.upper()

# Fix zip code: pad with leading zeros to make sure length is 5
data['customer_zip_code_prefix'] = data['customer_zip_code_prefix'].apply(lambda x: x.zfill(5))

# Check for missing values
print("\nMissing values per column:")
print(data.isnull().sum())

# Drop rows with any missing values
data_cleaned = data.dropna()

# Remove duplicates
duplicates_count = data_cleaned.duplicated().sum()
print(f"\nDuplicates found: {duplicates_count}")
data_cleaned = data_cleaned.drop_duplicates()

# Save cleaned data to CSV
cleaned_data_path = "C:/Users/su_te/Documents/olist-ecommerce-project/data/olist_customers_cleaned.csv"
data_cleaned.to_csv(cleaned_data_path, index=False)

print("\nCleaned data preview:")
print(data_cleaned.head())

print(f"\nCleaned data saved to: {cleaned_data_path}")