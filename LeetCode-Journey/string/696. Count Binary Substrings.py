def countBinarySubstrings(s):
    '''
    Approach:

    1️⃣ Count consecutive groups of same characters.
    2️⃣ For every adjacent pair of groups:
         add min(prev_group_length, curr_group_length).
    3️⃣ Return total count.
    '''

    prev_group = 0
    curr_group = 1
    result = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr_group += 1
        else:
            result += min(prev_group, curr_group)
            prev_group = curr_group
            curr_group = 1

    # Add last pair
    result += min(prev_group, curr_group)

    return result


# ====== INPUT / OUTPUT ======
s = input("Enter binary string: ")
print("Count of valid substrings:", countBinarySubstrings(s))
