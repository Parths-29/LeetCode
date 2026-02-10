'''
A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.
LeetCode-Journey.hash.3719. Longest Balanced Subarray I
'''
def longestBalancedSubarray(nums):
    n = len(nums)
    max_len = 0

    for start in range(n):
        even_set = set()
        odd_set = set()

        for end in range(start, n):
            # Add current number to even or odd set
            if nums[end] % 2 == 0:
                even_set.add(nums[end])
            else:
                odd_set.add(nums[end])

            # Check balance condition
            if len(even_set) == len(odd_set):
                max_len = max(max_len, end - start + 1)

    return max_len


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter array elements: ").split()))
print("Longest balanced subarray length:", longestBalancedSubarray(nums))
