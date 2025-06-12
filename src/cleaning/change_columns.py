# Iterates to only keep the columns that are valid for the analysis.
# Creates a column for value.

# function to remove columns from a dataframe.
def column_change_function(df):

    # remove the columns that are not needed for the analysis.
    columns_to_keep = ["full_name", "neo", "H", "diameter", "albedo", "spec_T"]
    columns_to_remove = [col for col in df.columns if col not in columns_to_keep]
    df_removed_columns = df.drop(columns=columns_to_remove)

    # return the new dataframe.
    return df_removed_columns