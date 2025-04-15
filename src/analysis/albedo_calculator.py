"""
Absolute magnitude (H) is the base brightness value for an object 1AU
from the Sun and 1AU from the observer and fully illuminated.
Lower H means brighter object.
Albedo can be calculated from the absolute magnitude (H) and the diameter (D)
of the object.
"""
import numpy as np
# estimate the albedo of an object using the absolute magnitude (H) and diameter (D)
def estimate_albedo(H, diameter):
    if H is None or diameter is None:
        return None
    
    albedo = ((1329 * np.power(10, -H/5)) / diameter)**2
    return albedo
