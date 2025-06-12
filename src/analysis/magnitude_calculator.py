"""
Absolute magnitude (H) is the base brightness value for an object.
Distances are assumed 1AU from the Sun and 1AU from the observer.
The object is assumed to be spherical and fully illuminated.
Lower H means brighter object.
H can be estimated from the diameter and albedo.
"""
import numpy as np

# estimate the magnitude of an asteroid based on its diameter and albedo
def estimate_magnitude(diameter, p):
    if diameter is None or p is None:
        return None
    
    return 5 * np.log10(1329 / (diameter * np.sqrt(p)))