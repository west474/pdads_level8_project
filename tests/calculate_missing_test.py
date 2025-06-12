import pandas as pd
from src.cleaning.calculate_missing import calculate_missing_values

def test_missing_value_calculator_with_real_data():
    test_data = [
        (None, 4.2, 0.31),  # Row 0
        (16.55, None, 0.51),  # Row 1
        (16.55, 1.554, None),  # Row 2
        (14.26, None, None),  # Row 3
        (None, None, 0.238),  # Row 4
        (None, None, None),  # Row 5
    ]

    df = pd.DataFrame(test_data, columns=['H', 'diameter', 'albedo'])
    df['spec_T'] = None

    calculate_missing_df = calculate_missing_values(df)

    # check there are 3 rows after calculation.
    assert len(calculate_missing_df) == 3

    # check that there are no nulls in H, diameter, albedo.
    for i, row in calculate_missing_df.iterrows():
        filled = row[["H", "diameter", "albedo"]]
        assert filled.notna().all(), \
            f'Expected no nulls in row {i}, but got {filled}'

    # check that spec_T is assigned.
    for i, row in calculate_missing_df.iterrows():
        assert row["spec_T"] in ["C", "S", "M"], \
            f'Expected spec_T to be C, S, or M in row {i}, but got {row["spec_T"]}'