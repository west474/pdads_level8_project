import numpy as np
from src.analysis.size_calculator import estimate_diameter

def test_estimate_diameter_with_real_data():
    # these test cases are based on real data from 
    # the JPL Small-Body Database that fall within 20% rtol.
    test_cases = [
        (13.80, 0.31, 4.2),   # 887 Alinda (A918 AA)
        (16.55, 0.51, 1.0),   # 1566 Icarus (1949 MA)
        (16.55, 0.184, 1.554), # 39572 (1993 DQ1)
        (14.26, 0.299, 3.512), # 68348 (2001 LO7)
        (9.18, 0.238, 37.675)  # 1036 Ganymed (A924 UB)
    ]

    # Loop through test cases and check expected diameter is correct
    for H, p, expected_diameter in test_cases:
        calculated = estimate_diameter(H, p)
        assert np.isclose(calculated, expected_diameter, rtol=0.20), \
            f"Expected ~{expected_diameter}, but got {calculated} for H={H}, p={p}"  # failure message