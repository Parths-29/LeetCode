def countPrimeSetBits(left, right):
    '''
    Approach:

    1️⃣ Predefine small primes up to 20.
    2️⃣ For each number in range:
         - Count set bits.
         - Check if count is prime.
    3️⃣ Return total count.
    '''

    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    count = 0

    for num in range(left, right + 1):
        set_bits = bin(num).count('1')
        if set_bits in primes:
            count += 1

    return count


# ====== INPUT / OUTPUT ======
left = int(input("Enter left: "))
right = int(input("Enter right: "))
print("Count of numbers with prime set bits:", countPrimeSetBits(left, right))