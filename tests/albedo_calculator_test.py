import numpy as np
from src.analysis.albedo_calculator import estimate_albedo

def test_estimate_albedo_with_real_data():
    # these test cases are based on real data from 
    # the JPL Small-Body Database that fall within 20% rtol.
    test_cases = [
        (13.80, 4.2, 0.31), # 887 Alinda (A918 AA)
        (16.55, 1.0, 0.51), # 1566 Icarus (1949 MA)
        (16.55, 1.554, 0.184), # 39572 (1993 DQ1)
        (14.26, 3.512, 0.299), # 68348 (2001 LO7)
        (9.18, 37.675, 0.238) # 1036 Ganymed (A924 UB)
    ]

# loop through test cases and check expected albedo is correct
    for H, D, expected_albedo in test_cases:
        calculated = estimate_albedo(H, D)
        assert np.isclose(calculated, expected_albedo, rtol=0.20), \
            f"Expected ~{expected_albedo}, but got {calculated} for H={H}, D={D}" # failure message