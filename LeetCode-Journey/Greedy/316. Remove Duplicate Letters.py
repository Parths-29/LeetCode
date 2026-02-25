def removeDuplicateLetters(s):
    '''
    Approach:

    1️⃣ Store last occurrence of each character.
    2️⃣ Use stack to build answer.
    3️⃣ If current char already used → skip.
    4️⃣ While stack top > current char
         and stack top appears later,
         pop from stack.
    5️⃣ Push current char.
    '''

    last_index = {ch: i for i, ch in enumerate(s)}
    stack = []
    used = set()

    for i, ch in enumerate(s):

        # Skip if already included
        if ch in used:
            continue

        # Maintain lexicographical order
        while (stack and
               ch < stack[-1] and
               last_index[stack[-1]] > i):
            removed = stack.pop()
            used.remove(removed)

        stack.append(ch)
        used.add(ch)

    return ''.join(stack)


# ====== INPUT / OUTPUT ======
s = input("Enter string: ")
print("Result:", removeDuplicateLetters(s))