def intToRoman(num):
    '''
    Approach:
    Use greedy subtraction.

    We maintain a list of values and their Roman symbols
    in descending order (including subtractive cases like 900, 400, etc.)

    For each value:
        While num >= value:
            Append symbol
            Subtract value from num

    Continue until num becomes 0.
    '''

    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    result = ""

    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]

    return result


# ====== INPUT / OUTPUT ======
num = int(input("Enter integer: "))
print("Roman numeral:", intToRoman(num))
