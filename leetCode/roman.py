import re

def roman_to_int(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for numeral in reversed(s):
        value = roman_numerals[numeral]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

def custom_sort(name):
    parts = name.split()
    return (parts[0], roman_to_int(parts[1]))

input_list = ["Louis IX", "Louis VIII"]
sorted_list = sorted(input_list, key=custom_sort)

print(sorted_list)
