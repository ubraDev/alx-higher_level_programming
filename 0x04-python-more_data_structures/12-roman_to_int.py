#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    prev_value = 0
    total_value = 0

    for char in reversed(roman_string):
        value = roman_numerals.get(char, 0)

        if value >= prev_value:
            total_value += value
        else:
            total_value -= value

        prev_value = value

    return (total_value)
