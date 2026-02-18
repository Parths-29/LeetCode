def hasAlternatingBits(n):
    '''
    Approach:

    1️⃣ Extract last bit using n % 2.
    2️⃣ Shift number right.
    3️⃣ Compare with new last bit.
    4️⃣ If two adjacent bits are same → return False.
    5️⃣ If loop completes → return True.
    '''

    prev_bit = n % 2
    n //= 2

    while n > 0:
        curr_bit = n % 2

        if curr_bit == prev_bit:
            return False

        prev_bit = curr_bit
        n //= 2

    return True


# ====== INPUT / OUTPUT ======
n = int(input("Enter number: "))
print("Has alternating bits:", hasAlternatingBits(n))
