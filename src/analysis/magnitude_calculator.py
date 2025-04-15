import numpy as np

# estimate the albedo of an object using the absolute magnitude (H) and diameter (D)
def estimate_magnitude(diameter, p):
    if diameter is None or p is None:
        return None
    
    return 5 * np.log10(1329 / (diameter * np.sqrt(p)))