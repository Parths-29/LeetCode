def partitionLabels(s):
    '''
    Approach:

    1️⃣ Store last occurrence of each character.
    2️⃣ Traverse string and keep updating partition end.
    3️⃣ When current index == end,
         close partition and record its size.
    '''

    # Step 1: Record last index of each character
    last_index = {}
    for i, ch in enumerate(s):
        last_index[ch] = i

    result = []
    start = 0
    end = 0

    # Step 2: Traverse and build partitions
    for i, ch in enumerate(s):
        end = max(end, last_index[ch])

        # If current index reaches partition end
        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


# ====== INPUT / OUTPUT ======
s = input("Enter string: ")
print("Partition sizes:", partitionLabels(s))