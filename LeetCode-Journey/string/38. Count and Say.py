def countAndSay(n):
    '''
    Approach:

    1️⃣ Start with base case "1".
    2️⃣ For each iteration:
         - Read previous string.
         - Count consecutive digits.
         - Append count + digit to new string.
    3️⃣ Repeat until reaching nth term.
    '''

    result = "1"

    for _ in range(2, n + 1):
        current = ""
        count = 1

        # Traverse previous result
        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                count += 1
            else:
                current += str(count) + result[i - 1]
                count = 1

        # Add last group
        current += str(count) + result[-1]

        result = current

    return result


# ====== INPUT / OUTPUT ======
n = int(input("Enter n: "))
print("Count and Say result:", countAndSay(n))
