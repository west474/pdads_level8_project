# iterates through completing rows and columns AFTER an initial clean.
import pandas as pd
from src.analysis import albedo_calculator, magnitude_calculator, size_calculator
from src.cleaning import spectral_assigner, remove_nulls

def calculate_missing_values(df):

    # remove rows with 2 or more missing values.
    df = remove_nulls.remove_nulls_pre_function(df)

    # fill missing values for H, diameter, and albedo.
    for idx, row in df.iterrows():
        # fill in missing H values.
        if pd.isna(row['H']) and not pd.isna(row['diameter']) and not pd.isna(row['albedo']):
            df.at[idx, 'H'] = magnitude_calculator.estimate_magnitude(row['diameter'], row['albedo'])

        # fill in missing albedo values.
        if pd.isna(row['albedo']) and not pd.isna(row['H']) and not pd.isna(row['diameter']):
            df.at[idx, 'albedo'] = albedo_calculator.estimate_albedo(row['H'], row['diameter'])

        # fill in missing diameter values.
        if pd.isna(row['diameter']) and not pd.isna(row['H']) and not pd.isna(row['albedo']):
            df.at[idx, 'diameter'] = size_calculator.estimate_diameter(row['H'], row['albedo'])

    # assign spectral type based on albedo.
    for idx, row in df.iterrows():
        if pd.notna(row['albedo']):
            df.at[idx, 'spec_T'] = spectral_assigner.assign_spectral_type(row['albedo'])

    # remove rows with any remaining null values.
    df = remove_nulls.remove_nulls_post_function(df)
    return df