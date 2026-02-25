def sortByBits(arr):
    '''
    Approach:

    1️⃣ Define a key function:
         - First sort by number of set bits.
         - Then sort by value itself.
    2️⃣ Use built-in sort with custom key.
    '''

    return sorted(arr, key=lambda x: (bin(x).count('1'), x))


# ====== INPUT / OUTPUT ======
arr = list(map(int, input("Enter numbers: ").split()))
print("Sorted by bit count:", sortByBits(arr))