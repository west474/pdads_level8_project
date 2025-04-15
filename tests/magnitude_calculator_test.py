import numpy as np
from src.analysis.magnitude_calculator import estimate_magnitude

def test_estimate_magnitude_with_real_data():

    test_cases = [
        (0.31, 4.2, 13.80),     # 887 Alinda (A918 AA)
        (0.51, 1.0, 16.55),     # 1566 Icarus (1949 MA)
        (0.184, 1.554, 16.55),  # 39572 (1993 DQ1)
        (0.299, 3.512, 14.26),  # 68348 (2001 LO7)
        (0.238, 37.675, 9.18)   # 1036 Ganymed (A924 UB)
    ]

    # loop through test cases and check expected albedo is correct
    for p, D, expected_magnitude in test_cases:
        calculated = estimate_magnitude(D, p)
        assert np.isclose(calculated, expected_magnitude, rtol=0.20), \
            f"Expected ~{expected_magnitude}, but got {calculated} for p={p}, D={D}" # failure message