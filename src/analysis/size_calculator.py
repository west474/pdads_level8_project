"""
Absolute magnitude (H) is the base brightness value for an object 1AU
from the Sun and 1AU from the observer and fully illuminated.
Lower H means brighter object.
Albedo can be calculated from the absolute magnitude (H) and the diameter (D)
of the object.
"""
import numpy as np
# estimate the diameter of an object using the absolute magnitude (H) and albedo
def estimate_diameter(H, p):
    if H is None or p is None:
        return None
    
    diameter = (1329 / np.sqrt(p)) * np.power(10, -H/5)
    return diameter