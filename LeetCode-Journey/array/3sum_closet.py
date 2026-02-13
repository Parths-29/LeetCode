''' 
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)

    # Start with the sum of first three elements
    closest_sum = nums[0] + nums[1] + nums[2]

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            # Update closest sum if this is nearer to target
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum

            # Move pointers to get closer to target
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                # Exact match found
                return curr_sum

    return closest_sum


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))
print("Closest sum:", threeSumClosest(nums, target))
