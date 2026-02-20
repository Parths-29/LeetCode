def makeLargestSpecial(s):
    '''
    Approach:

    1️⃣ Treat 1 as '(' and 0 as ')'.
    2️⃣ Split into top-level special substrings.
    3️⃣ For each substring:
         - Remove outer 1 and 0
         - Recursively process inside
         - Add outer 1 and 0 back
    4️⃣ Sort substrings in reverse order.
    5️⃣ Join and return.
    '''

    count = 0
    start = 0
    blocks = []

    for i in range(len(s)):
        if s[i] == '1':
            count += 1
        else:
            count -= 1

        # When balanced, we found a special block
        if count == 0:
            # Recursively process inside
            inner = makeLargestSpecial(s[start + 1:i])
            blocks.append("1" + inner + "0")
            start = i + 1

    # Sort blocks in descending order
    blocks.sort(reverse=True)

    return "".join(blocks)


# ====== INPUT / OUTPUT ======
s = input("Enter special binary string: ")
print("Largest special string:", makeLargestSpecial(s))