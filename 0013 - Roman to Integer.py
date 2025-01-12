def roman_to_int(s: str) -> int:
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    parts = list(s)
    total = 0
    last_value = 0

    for part in parts:
        value = roman_numbers[part]

        if last_value < value:
            total += value - (last_value * 2)
        else:
            total += value
        last_value = value


    return total


if __name__ == '__main__':
    print(roman_to_int('III')) # Expected 3
    print(roman_to_int('LVIII')) # Expected 58
    print(roman_to_int('MCMXCIV')) # Expected 1994
