# removes nulls after calculations.

# specify columns to check for nulls.
main_columns = ['H', 'diameter', 'albedo']

def remove_nulls_pre_function(df):

    # remove rows with 2 or more missing values.
    df_removed_nulls = df[df[main_columns].isna().sum(axis=1) < 2]
    return df_removed_nulls

def remove_nulls_post_function(df):
    df_removed_nulls = df.dropna(subset=main_columns)
    return df_removed_nulls
