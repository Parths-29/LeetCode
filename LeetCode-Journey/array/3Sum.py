#so in this question the ps is -Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.
# now this question is a classic one and the approach to solve this is - sort the array and then use two pointers to find pairs that sum up to the negative of the current element. We also need to skip duplicates to ensure unique triplets in the result.
# approach - Sorting allows two-pointer traversal then fix one element → solve remaining as 2Sum duplicate skipping prevents repeated triplets
def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue   # skip duplicate fixed element

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # skip duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter array elements: ").split()))
print("Triplets:", threeSum(nums))
