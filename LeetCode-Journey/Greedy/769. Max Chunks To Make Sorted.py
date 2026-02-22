def maxChunksToSorted(arr):
    '''
    Approach:

    1️⃣ Keep track of maximum value seen so far.
    2️⃣ If max_so_far == current index,
         we can form a chunk here.
    3️⃣ Count such positions.
    '''

    max_so_far = 0
    chunks = 0

    for i in range(len(arr)):
        max_so_far = max(max_so_far, arr[i])

        if max_so_far == i:
            chunks += 1

    return chunks


# ====== INPUT / OUTPUT ======
arr = list(map(int, input("Enter permutation: ").split()))
print("Maximum chunks:", maxChunksToSorted(arr))