''' 
Question - two pointers: 31. Next Permutation (Medium)
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

---
My Approach (Array Traversal / Two Pointers):
1. Find the Pivot: Traverse the array from right to left to find the first element that is smaller than the element directly to its right (`nums[i] < nums[i+1]`). This element is our "pivot".
2. Handle the Edge Case: If we scan the whole array and don't find a pivot, it means the array is sorted in strictly descending order (like `[3, 2, 1]`). This is the absolute largest permutation. The problem states we just need to reverse the whole array to get the smallest permutation.
3. Find the Successor: If we did find a pivot, we scan from the right side of the array again to find the smallest number that is strictly greater than our pivot.
4. Swap: Swap the pivot and the successor.
5. Reverse the Suffix: After the swap, the numbers to the right of the original pivot index are still in descending order. We reverse that sub-array to make it strictly ascending. This guarantees we get the *next* permutation, not a permutation much further down the line.

Time Complexity: O(N) where N is the length of the array. We do at most 3 passes over the array.
Space Complexity: O(1) as we modify the array strictly in-place.
'''

import ast
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1
        
        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
                
        if pivot == -1:
            # Step 2: If the array is strictly descending, just reverse it
            nums.reverse()
            return
            
        # Step 3 & 4: Find the next greater element from the right and swap
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break
                
        # Step 5: Reverse the suffix starting right after the pivot index
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 31. Next Permutation Interactive Runner ---")
    try:
        user_input = input("Enter the nums array (e.g., [1,2,3]): ")
        
        # Safely evaluate the input string into a Python list
        parsed_nums = ast.literal_eval(user_input) 
        
        if not isinstance(parsed_nums, list):
            raise ValueError("Input must be a list.")
            
        # Call the function (modifies the list in-place, returns None)
        solution.nextPermutation(parsed_nums)
        
        # Print the modified list
        print(f"\nOutput: {parsed_nums}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")