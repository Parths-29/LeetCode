'''
Docstring for LeetCode-Journey.array.47. Permutations II
47. Permutations II
Solved
Medium
Topics
premium lock icon
Companies
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''

## so my approach is basically while during backtracking: skip a number if it is the same as previous and previous duplicate was not used in this level
def permuteUnique(nums):
    nums.sort()  # sort to group duplicates
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        # If permutation complete
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            # Skip if already used
            if used[i]:
                continue

            # Skip duplicates:
            # If same as previous and previous wasn't used,
            # it means we already explored this branch
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            # Choose
            path.append(nums[i])
            used[i] = True

            # Explore
            backtrack()

            # Undo
            path.pop()
            used[i] = False

    backtrack()
    return result


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter array elements: ").split()))
print("Unique Permutations:", permuteUnique(nums))
