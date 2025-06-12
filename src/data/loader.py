import pandas as pd

# loads the data from a CSV file into a pandas DataFrame.
def data_loading_function(filepath):
    df = pd.read_csv(filepath, low_memory=False)
    df = df.dropna(how='all') # remove empty rows from the csv file.
    return df

# saves the DataFrame to a CSV file.
def data_saving_function(data, filepath):
    data.to_csv(filepath, index=False)