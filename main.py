import pandas as pd
from src.data.processor import data_processing_function
from src.visualisation import data_visualisation as vis

def main():
    # load the original csv in for cleaning.
    raw_filepath = './data/raw/sbdb_query_results.csv'
    cleaned_filepath = './data/cleaned/cleaned_data.csv'

    # process the data.
    data_processing_function(raw_filepath, cleaned_filepath)

    # output the visualisations.
    df_clean = pd.read_csv(cleaned_filepath)
    vis.barchart(df_clean)
    vis.violinplot(df_clean)
    vis.scatterplot(df_clean)
    vis.piechart(df_clean)

if __name__ == "__main__":
    main()