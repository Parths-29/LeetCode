def binaryGap(n):
    '''
    Approach:

    1️⃣ Traverse bits from right to left.
    2️⃣ Track position of last seen 1.
    3️⃣ When another 1 appears,
         compute distance and update max.
    4️⃣ Return maximum distance found.
    '''

    last_pos = -1
    max_gap = 0
    position = 0

    while n > 0:
        if n & 1:  # Check if last bit is 1
            if last_pos != -1:
                max_gap = max(max_gap, position - last_pos)
            last_pos = position

        n >>= 1
        position += 1

    return max_gap


# ====== INPUT / OUTPUT ======
n = int(input("Enter number: "))
print("Longest binary gap:", binaryGap(n))