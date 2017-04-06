"""
Roman numerals decoder
---------------
Input: string, containing a valid roman numeral
Returns an integer (Arabic numeral representation of the Roman numeral)
"""


base_numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def decode(roman):
    arabic = 0
    len_roman = len(roman)
    for i in range(len_roman):
        current_value = base_numbers[roman[i]]

        # if the current item is smaller than the next one, subtract
        if i + 1 != len_roman and base_numbers[roman[i + 1]] > current_value:
            arabic -= current_value
            continue

        arabic += current_value

    return arabic

assert decode('CMVII') == 907