def nextPermutation(nums):
    n = len(nums)

    # 1️⃣ Find the first index from the right where nums[i] < nums[i + 1]
    # This is the point where we can make the permutation bigger
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # 2️⃣ If such index exists, find the next bigger element on the right
    if i >= 0:
        j = n - 1
        # Find the smallest number greater than nums[i]
        while nums[j] <= nums[i]:
            j -= 1
        # Swap them to make the number just slightly bigger
        nums[i], nums[j] = nums[j], nums[i]

    # 3️⃣ Reverse everything after index i
    # This makes the suffix the smallest possible (lexicographically)
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter array elements: ").split()))
nextPermutation(nums)
print("Next permutation:", nums)
