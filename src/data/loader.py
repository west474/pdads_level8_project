import pandas as pd

'''
Author: Richard West
This module is responsible for loading and saving data.
It contains functions to read and write CSV files.
'''

# this loads the data from a CSV file into a pandas DataFrame.
def load_data(filepath):
    return pd.read_csv(filepath)

# this saves the DataFrame to a CSV file.
def save_data(data, filepath):
    data.to_csv(filepath, index=False)