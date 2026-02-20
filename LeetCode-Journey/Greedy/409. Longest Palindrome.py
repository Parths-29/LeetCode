def longestPalindrome(s):
    '''
    Approach:

    1️⃣ Count frequency of each character.
    2️⃣ Add all even counts fully.
    3️⃣ For odd counts, add (count - 1).
    4️⃣ If at least one odd exists, add 1 for center.
    '''

    from collections import Counter

    freq = Counter(s)
    length = 0
    odd_found = False

    for count in freq.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True

    if odd_found:
        length += 1

    return length


# ====== INPUT / OUTPUT ======
s = input("Enter string: ")
print("Longest palindrome length:", longestPalindrome(s))