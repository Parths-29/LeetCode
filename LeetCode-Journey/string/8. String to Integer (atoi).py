'''
Intuition Think of this like reading a messy handwritten number on a form. First, you ignore the scribbles in the margin (whitespace). Then, you check if there is a plus or minus sign. Finally, you just read the digits until you hit something that is not a number, like a letter. If the number is too big to fit in the box, you just write the biggest number that fits.
Approach - 
We process the string in three simple stages:
1. Trim: We skip over any leading spaces.
2. Sign: We check the very next character for a + or - to decide if we are going positive or negative.
3. Build: We loop through the remaining characters. If it is a digit, we add it to our number. If it is not, we stop immediately. Finally, we make sure the result stays within the 32-bit limit using min and max.
'''
def myAtoi(s):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    i = 0
    n = len(s)

    # 1️⃣ Skip leading whitespaces
    while i < n and s[i] == " ":
        i += 1

    # If string is empty after spaces
    if i == n:
        return 0

    # 2️⃣ Check sign
    sign = 1
    if s[i] == "-":
        sign = -1
        i += 1
    elif s[i] == "+":
        i += 1

    result = 0

    # 3️⃣ Read digits
    while i < n and s[i].isdigit():
        digit = int(s[i])

        # 4️⃣ Check overflow before updating result
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN

        result = result * 10 + digit
        i += 1

    return sign * result


# ====== INPUT / OUTPUT ======
s = input("Enter string: ")
print("Converted integer:", myAtoi(s))
