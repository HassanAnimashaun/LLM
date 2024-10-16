import pandas as pd

# Function to clean and format the dataset
def clean_and_format_dataset(df):
    # 1. Show the number of missing values per column
    missing_values = df.isnull().sum()
    print("Missing Values Per Column:\n", missing_values)
    
    # 2. Show columns with incorrect data types
    incorrect_types = df.dtypes[df.dtypes == 'object']  # Assuming incorrect types are non-numeric for numeric columns
    print("\nColumns with Incorrect Data Types:\n", incorrect_types)

    # 3. Convert data types where applicable (this step assumes non-numeric columns need conversion)
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='ignore')
        except:
            continue
    
    # Return the cleaned dataset
    return df

# Load the dataset (replace with the correct file path)
file_path = 'your_dataset.csv'
dataset = pd.read_csv(file_path)

# Apply the cleaning function
cleaned_dataset = clean_and_format_dataset(dataset)

# Save the cleaned dataset if necessary
cleaned_dataset.to_csv('cleaned_dataset.csv', index=False)
