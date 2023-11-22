### Thomas Silva
### ENGR 103 Assignment 8a.
### Nov 22, 2023.


def count_letters(input_string):
    letter_counts = {}

    for char in input_string:
        if char.isalpha():
            upper_char = char.upper()

            letter_counts[upper_char] = letter_counts.get(upper_char, 0) + 1

    return letter_counts

input_str = "Black and Yellow"
result = count_letters(input_str)
print(result)
