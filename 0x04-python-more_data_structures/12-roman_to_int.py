#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_letters = {
                     "I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000
                    }
    decimal = 0
    prev = 32864
    for char in roman_string:
        num = roman_letters[char.upper()]
        if num <= prev:
            decimal += num
        else:
            decimal += (num - (prev * 2))
        prev = num
    return decimal
