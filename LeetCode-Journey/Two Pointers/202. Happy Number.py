'''
Question: 167. Two Sum II - Input Array Is Sorted (Medium)
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers, each incremented by one, as an integer array [index1, index2].
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

---
My Approach (Two Pointers):
1. Initialize two pointers: `left` at the beginning of the array (0), and `rght` at the end (n - 1).
2. Start a loop to converge the pointers. At each step, calculate the sum (`sm`) of the elements at the two pointers.
3. If `sm == target`: We found our pair! Since the problem requires 1-indexed results, return `[left + 1, rght + 1]`.
4. If `sm < target`: Because the array is sorted, the only way to increase the sum is to move the `left` pointer to the right.
5. If `sm > target`: The sum is too large. The only way to decrease it is to move the `rght` pointer to the left.
6. The problem guarantees a solution exists, so the pointers will definitely meet at the correct numbers.

Time Complexity: O(N) where N is the length of the numbers array.
Space Complexity: O(1) extra space.
'''

import ast
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, rght =  0, n - 1

        for _ in range(n):
            sm = numbers[left] + numbers[rght]

            if sm == target:
                return [left + 1, rght + 1]

            if sm < target: 
                left += 1
            else: 
                rght -= 1

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 167. Two Sum II Interactive Runner ---")
    try:
        numbers_input = input("Enter the numbers array (e.g., [2,7,11,15]): ")
        target_input = input("Enter the target integer (e.g., 9): ")
        
        parsed_numbers = ast.literal_eval(numbers_input)
        target = int(target_input)
        
        if not isinstance(parsed_numbers, list):
            raise ValueError("Numbers input must be a list.")
            
        result = solution.twoSum(parsed_numbers, target)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")