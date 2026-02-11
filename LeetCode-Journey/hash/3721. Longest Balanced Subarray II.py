'''
You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.
'''
def longestBalancedSubarray(nums):
    even_set = set()
    odd_set = set()

    # Map to store first occurrence of each diff
    diff_index = {0: -1}

    max_len = 0

    for i in range(len(nums)):
        # Add number to correct set
        if nums[i] % 2 == 0:
            even_set.add(nums[i])
        else:
            odd_set.add(nums[i])

        # Calculate current difference
        diff = len(even_set) - len(odd_set)

        # If diff seen before → subarray is balanced
        if diff in diff_index:
            max_len = max(max_len, i - diff_index[diff])
        else:
            # Store first time we see this diff
            diff_index[diff] = i

    return max_len


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter array elements: ").split()))
print("Longest balanced subarray length:", longestBalancedSubarray(nums))
