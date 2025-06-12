from src.cleaning.spectral_assigner import assign_spectral_type

def test_spectral_assignment_with_generic_data():

    test_cases = [
        (0.07, "S"),     
        (0.069, "C"),    
        (0.071, "S"),    
        (0.22, "S"),     
        (0.221, "M"),
        (0.23, "M"),    
        (0.22, "S"),     
        (0.221, "M"),
        (0.069, "C"),    
        (0.22, "S"),     
        (0.221, "M"), 
    ]

    # check if the function correctly assigns spectral types based on albedo.
    for albedo, expected in test_cases:
        result = assign_spectral_type(albedo)
        assert result == expected, \
            f"Albedo {albedo} expected {expected} but got {result}"