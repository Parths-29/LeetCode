'''
Question: 1534. Count Good Triplets (Easy)
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
- 0 <= i < j < k < arr.length
- |arr[i] - arr[j]| <= a
- |arr[j] - arr[k]| <= b
- |arr[i] - arr[k]| <= c
Return the number of good triplets.

Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

---
My Approach (Optimized Brute Force with Early Pruning):
1. The constraints for this problem are small enough (N <= 100) that a 3-pointer $O(N^3)$ approach is the expected solution.
2. We iterate `i` from the start, `j` from `i + 1`, and `k` from `j + 1`.
3. Elite Optimization: Instead of evaluating all three conditions in the innermost loop, we evaluate `|arr[i] - arr[j]| <= a` in the second loop. 
4. If `i` and `j` already violate the first rule, we completely skip the `k` loop, pruning a massive amount of unnecessary computational branches.

Time Complexity: Worst case $O(N^3)$, but drastically faster in practice due to early branch pruning.
Space Complexity: $O(1)$ auxiliary space.
'''

import ast
from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets = 0
        length = len(arr)

        for i in range(length):  # i is the first index
            for j in range(i + 1, length):  # j must be after i
                
                # EARLY PRUNING: Only run the k loop if the first condition is already met!
                if abs(arr[i] - arr[j]) <= a:  
                    for k in range(j + 1, length):  # k must be after j
                        
                        # Check the remaining two conditions
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_triplets += 1
                            # 🥋 Rock Lee: "Another success from persistence!" 🥳
        
        return good_triplets

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1534. Count Good Triplets Interactive Runner ---")
    try:
        arr_input = input("Enter the arr (e.g., [3,0,1,1,9,7]): ").strip()
        a_input = input("Enter a: ").strip()
        b_input = input("Enter b: ").strip()
        c_input = input("Enter c: ").strip()
        
        # Safely evaluate inputs
        parsed_arr = ast.literal_eval(arr_input)
        parsed_a = int(a_input)
        parsed_b = int(b_input)
        parsed_c = int(c_input)
        
        if not isinstance(parsed_arr, list):
            raise ValueError("arr must be a list of integers.")
            
        # Calling the function
        result = solution.countGoodTriplets(parsed_arr, parsed_a, parsed_b, parsed_c)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")