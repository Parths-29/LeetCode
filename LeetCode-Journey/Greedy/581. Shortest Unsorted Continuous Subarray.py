def findUnsortedSubarray(nums):
    '''
    Approach:

    1️⃣ Traverse left to right to find right boundary.
       If nums[i] < max_so_far → update right.

    2️⃣ Traverse right to left to find left boundary.
       If nums[i] > min_so_far → update left.

    3️⃣ Return right - left + 1.
    '''

    n = len(nums)
    left, right = -1, -1

    # Step 1: Find right boundary
    max_so_far = float('-inf')
    for i in range(n):
        max_so_far = max(max_so_far, nums[i])
        if nums[i] < max_so_far:
            right = i

    # Step 2: Find left boundary
    min_so_far = float('inf')
    for i in range(n - 1, -1, -1):
        min_so_far = min(min_so_far, nums[i])
        if nums[i] > min_so_far:
            left = i

    if right == -1:
        return 0

    return right - left + 1


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter numbers: ").split()))
print("Length of shortest unsorted subarray:", findUnsortedSubarray(nums))