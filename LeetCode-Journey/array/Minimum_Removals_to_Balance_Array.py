def minRemovals(nums, k):
    nums.sort()
    n = len(nums)

    l = 0
    max_len = 0

    for r in range(n):
        while nums[r] > nums[l] * k:
            l += 1
        max_len = max(max_len, r - l + 1)

    return n - max_len


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))
print("Minimum removals:", minRemovals(nums, k))
