#!/usr/bin/python3
def add_integer(a, b=98):
    # Check if both a and b are either integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Calculate the addition and return the result as an integer
    result = a + b
    return result
