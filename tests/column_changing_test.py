from src.cleaning.change_columns import column_change_function
import pandas as pd

# test function to check if the column_change_function works as expected.
def test_column_change_function():
    
    test_data = {
        "full_name": ["A", "B", "C"],
        "neo": [True, False, True],
        "H": [1.0, 2.0, 3.0],
        "diameter": [10.0, 20.0, 30.0],
        "albedo": [0.1, 0.2, 0.3],
        "spec_T": ["S", "C", "M"],
        "extra_column_1": [100, 200, 300],
        "extra_column_2": [400, 500, 600]
    }
    
    # test the column_change_function.
    df = pd.DataFrame(test_data)
    column_change_df = column_change_function(df)
    
    # check columns against expected.
    expected_columns = ["full_name", "neo", "H", "diameter", "albedo", "spec_T"]
    assert all(col in column_change_df.columns for col in expected_columns), \
        f"Expected columns {expected_columns} but got {column_change_df.columns.tolist()}"
    
    # check no extra columns.
    assert not any(col in column_change_df.columns for col in ["extra_column_1", "extra_column_2"]), \
        f"Extra columns should have been removed but found {column_change_df.columns.tolist()}"