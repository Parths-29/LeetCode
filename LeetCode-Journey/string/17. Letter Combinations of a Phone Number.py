def letterCombinations(digits):
    '''
    Approach:

    1️⃣ Map digits to letters like telephone keypad.
    2️⃣ Use backtracking to build combinations.
    3️⃣ For each digit, try all possible letters.
    4️⃣ When current string length equals digits length,
        add it to result.
    '''

    if not digits:
        return []

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def backtrack(index, path):
        # If combination complete
        if index == len(digits):
            result.append(path)
            return

        # Get letters for current digit
        letters = phone[digits[index]]

        for letter in letters:
            # Choose
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return result


# ====== INPUT / OUTPUT ======
digits = input("Enter digits (2-9 only): ")
print("Letter combinations:", letterCombinations(digits))
