"""
Space objects (NEO in this case) can be classified into spectral types based on the albedo.
Estimating the albedo can help in determining the spectral type.
Albedo can be calculated if absolute magnitude (H), and diameter (D) are known.
This script provides a function to estimate albedo using H and D.
"""
import numpy as np

# estimate the albedo of an object using the absolute magnitude (H) and diameter (D).
def estimate_albedo(H, diameter):

    if H is None or diameter is None:
        return None
    
    albedo = ((1329 * np.power(10, -H/5)) / diameter)**2
    return albedo
