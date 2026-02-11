'''
Docstring for LeetCode-Journey.array.46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]'''
def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        # If current permutation is complete
        if len(path) == len(nums):
            result.append(path[:])  # copy the permutation
            return

        # Try every number
        for i in range(len(nums)):
            if used[i]:
                continue  # skip if already used

            # Choose the number
            path.append(nums[i])
            used[i] = True

            # Explore further
            backtrack()

            # Undo choice (backtrack step)
            path.pop()
            used[i] = False

    backtrack()
    return result


# ====== INPUT / OUTPUT ======
nums = list(map(int, input("Enter array elements: ").split()))
print("Permutations:", permute(nums))
