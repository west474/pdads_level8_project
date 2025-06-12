
'''
Spectral groups can be estimated using albedo.
Low albedo (<0.07) asteroids are typically of C/D/P type.
Medium albedo (0.07-0.22) asteroids are typically of S/Q/K type.
High albedo (>0.22) asteroids are typically of M/E/V type.

I have simplified the classification to three groups for the data set:
C (carbonaceous), S (silicate), and M (metallic).
'''

# estimate the spectral type of an asteroid based on its albedo.
def assign_spectral_type(albedo):

    if albedo is None:
        return None
    
    elif albedo < 0.07:
        return 'C' # low albedo, carbonaceous type
    elif 0.07 <= albedo <= 0.22:
        return 'S' # medium albedo, silicate type
    elif albedo > 0.22:
        return 'M' # high albedo, metallic type
    else:
        return None 