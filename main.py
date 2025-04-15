from src.data.loader import load_data, save_data
from src.data.processor import process_data

def main():
    # load the original csv in for cleaning
    raw_filepath = './data/raw/sbdb_query_results.csv'

    df = load_data(raw_filepath)

if __name__ == "__main__":
    main()
