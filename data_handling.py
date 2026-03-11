import pandas as pd
import re

#-------- Functions for data handling and cleaning --------

# Cleaning the data so that the column names are 
def clean_columns(df):
    """retrieves and cleans column names so that they display correctly in the app"""
    df.columns = [re.sub(r'(_)', ' ', col).title() for col in df.columns]
    return df

# Percentage to numeric conversion
def convert_percentage_to_numeric(df, column_name):
    """Converts percentage strings to numeric values in the specified column."""

    #check if the column is of object type and contains percentage values
    if df[column_name].dtype == "object":
        if df[column_name].str.endswith('%').any():

            #Remove the percentage sign, convert to float, and divide by 100 to get the numeric value
            df[column_name] = df[column_name].str.rstrip('%').astype(float) / 100        
    return df

# Function to load and clean data
def load_and_clean_data(file_path):
    """Loads a dataset from the specified file path and applies cleaning functions."""
    df = pd.read_csv(file_path)
    df = clean_columns(df)
    # Example: Convert a specific percentage column to numeric if it exists
    percentage_columns = [col for col in df.columns if 'Percentage' in col or '%' in col]
    for col in percentage_columns:
        df = convert_percentage_to_numeric(df, col)
    return df