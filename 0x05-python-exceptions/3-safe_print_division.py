#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b  # Attempt to perform the division
    except (TypeError, ZeroDivisionError):  # Handle division by zero or type error
        div = None  # Set div to None in case of error
    finally:
        print("Inside result: {}".format(div))  # Always print the result, regardless of error
    return div  # Return the division result or None

# Test cases
a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
