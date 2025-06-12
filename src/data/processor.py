from src.cleaning import change_columns, calculate_missing
from src.data import loader

def data_processing_function(raw_filepath, cleaned_filepath):

    # load raw csv file.
    df = loader.data_loading_function(raw_filepath)

    # remove unnecessary columns.
    df_1 = change_columns.column_change_function(df)

    # calculate missing values.
    df_2 = calculate_missing.calculate_missing_values(df_1)

    # save the cleaned dataframe.
    df_processed = loader.data_saving_function(df_2, cleaned_filepath)

    return df_processed