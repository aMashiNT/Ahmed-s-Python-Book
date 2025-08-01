# Default Arguments

def power(base, exponent=2):
    """
    Raises base to the given exponent.
    If exponent not provided, squares the base.
    """
    return base ** exponent

print(power(5))      # 5² = 25  
print(power(3, 3))   # 3³ = 27  
