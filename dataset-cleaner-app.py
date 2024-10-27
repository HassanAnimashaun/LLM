import pandas as pd
import numpy as np

def downsize_dataset(file_path, output_path, sample_fraction=0.03):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Downsize by sampling 3% of the dataset
    downsized_data = data.sample(frac=sample_fraction, random_state=42)

    # Save the downsized dataset to a new file
    downsized_data.to_csv(output_path, index=False)

    print(f"Downsized dataset saved to {output_path} with {len(downsized_data)} records out of {len(data)}.")
    return downsized_data

# Example usage
file_path = 'dataset.csv'   # Replace with actual dataset path
output_path = 'downsized_dataset.csv'   # Replace with desired output path
downsized_data = downsize_dataset(file_path, output_path)
