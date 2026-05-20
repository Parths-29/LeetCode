'''
Question: 2657. Find the Prefix Common Array of Two Arrays (Medium)
You are given two 0-indexed integer permutations A and B of length n.
A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
Return the prefix common array of A and B.

---
My Approach (Single-Pass Frequency Tracker):
1. A brute force approach checking every prefix backward takes O(N^3) or O(N^2) time.
2. Because A and B are permutations of numbers 1 to N, a number can appear at most twice across both arrays.
3. We maintain a `freq` array to count how many times we've seen each number.
4. We iterate through A and B simultaneously with a single loop.
5. We increment the frequency of A[i]. If it reaches 2, it means we've now seen it in both arrays, so we increment our running `common` count.
6. We do the exact same for B[i]. 
7. We append the running `common` count to our result array `ans` at each step.

Time Complexity: O(N) where N is the length of the arrays. We visit each index exactly once.
Space Complexity: O(N) to store the frequency array and the result array. Because N is small, this RAM footprint is microscopic compared to allocating multiple sets or running nested loops.
'''

import ast
from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []
        
        # Frequency array to track occurrences of numbers 1 through n
        # We use n + 1 so the indices perfectly match the numbers 1 to N
        freq = [0] * (n + 1)
        common = 0

        for i in range(n):
            # Process the element from array A
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1
                
            # Process the element from array B
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1
                
            # Store the current prefix intersection count
            ans.append(common)

        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 2657. Prefix Common Array Interactive Runner ---")
    try:
        a_input = input("Enter array A (e.g., [1,3,2,4]): ").strip()
        b_input = input("Enter array B (e.g., [3,1,2,4]): ").strip()
        
        # Safely evaluate inputs
        parsed_A = ast.literal_eval(a_input)
        parsed_B = ast.literal_eval(b_input)
        
        if not isinstance(parsed_A, list) or not isinstance(parsed_B, list):
            raise ValueError("Inputs must be valid lists of integers.")
            
        result = solution.findThePrefixCommonArray(parsed_A, parsed_B)
        print(f"\nPrefix Common Array: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")