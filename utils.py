
# utils.py

import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """
    Clean the DataFrame by performing basic cleaning operations.
    """
    if df is None:
        return None
    
    # Remove duplicates
    df = df.drop_duplicates()
    # Drop rows with missing values
    df = df.dropna()
    # Strip whitespace from column names
    df.columns = [col.strip() for col in df.columns]
    
    return df