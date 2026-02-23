def arrayPairSum(nums):
    '''
    Approach:

    1️⃣ Sort the array.
    2️⃣ Pair consecutive elements.
    3️⃣ Sum every second element (min of each pair).
    '''

    nums.sort()
    return sum(nums[::2])


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter numbers: ").split()))
print("Maximum sum of pair minimums:", arrayPairSum(nums))