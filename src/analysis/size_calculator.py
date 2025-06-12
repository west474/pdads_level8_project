"""
Diameter is the estimated size of an object based on its absolute magnitude (H) and albedo (p).
This module provides a function to estimate the diameter of an object.
"""
import numpy as np
# estimate the diameter of an object using the absolute magnitude (H) and albedo
def estimate_diameter(H, p):
    if H is None or p is None:
        return None
    
    diameter = (1329 / np.sqrt(p)) * np.power(10, -H/5)
    return diameter