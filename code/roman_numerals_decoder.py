"""
Roman numerals decoder
---------------
Input: string, containing a valid roman rumeral
Returns an integer (Arabic numeral representation of the Roman numeral)
"""


base_numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def decode(roman):
    arabic = 0
    for i in range(len(roman)):
        current = roman[i]
        current_value = base_numbers[current]

        # if the current item is smaller than the next one skip this iteration
        if i + 1 != len(roman) and base_numbers[roman[i + 1]] > current_value:
            continue

        # if we have a prefix, subtract
        if i != 0 and base_numbers[roman[i - 1]] < current_value:
            arabic -= base_numbers[roman[i - 1]]

        arabic += current_value

    return arabic

assert decode('CMVII') == 907