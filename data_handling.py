import pandas as pd
import re

#-------- Functions for data handling and cleaning --------

# Cleaning the data so that the column names are 
def clean_data(data):
    """Clean and format the column names in the data."""
    data.columns = [re.sub(r'(_)', ' ', col).title() for col in data.columns]
    return data