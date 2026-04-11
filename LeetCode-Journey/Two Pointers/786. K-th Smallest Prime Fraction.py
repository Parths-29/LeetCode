'''
Question: 786. K-th Smallest Prime Fraction (Medium/Hard)
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Example 1:
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

---
My Approach (Binary Search on Value Space + Two Pointers):
1. Instead of using a Min-Heap which takes O(N) space, we can binary search the actual floating-point value of the fraction between 0.0 and 1.0.
2. For a given `mid` value, we want to count how many fractions `arr[i] / arr[j]` are less than or equal to `mid`.
3. Because the array is sorted, we can use a two-pointer sliding window. For each numerator `arr[i]`, we slide the denominator `arr[j]` until the fraction is smaller than `mid`. 
4. All remaining elements from `j` to the end of the array will also form valid fractions smaller than `mid`, so we add `n - j` to our total count.
5. While counting, we also keep track of the maximum actual fraction (`max_frac`) we encountered that is <= `mid`. 
6. If our total count perfectly matches `k`, we know `max_frac` is our exact answer. Adjust the binary search bounds otherwise.

Time Complexity: $O(N \log M)$ where N is the length of the array and M is the precision of the binary search.
Space Complexity: $O(1)$ auxiliary space, a massive optimization over the $O(N)$ Heap approach.
'''

import ast
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0
        res = []

        while left <= right:
            mid = left + (right - left) / 2
            j = 1
            total = 0
            num, den = 0, 0
            max_frac = 0.0
            
            for i in range(n):
                # Slide the denominator until the fraction is strictly less than or equal to mid
                while j < n and arr[i] >= arr[j] * mid:
                    j += 1
                
                # All remaining elements to the right are even larger denominators, 
                # so they will make the fraction even smaller. Add them all to total!
                total += (n - j)

                # Keep track of the largest valid fraction we've seen in this sweep
                if j < n and max_frac < (arr[i] / arr[j]):
                    max_frac = arr[i] / arr[j]
                    num, den = i, j

            # If we found exactly k fractions smaller than mid, our tracked max_frac is the answer
            if total == k:
                res = [arr[num], arr[den]]
                break

            # Standard binary search adjustments
            if total > k:
                right = mid
            else:
                left = mid

        return res

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 786. K-th Smallest Prime Fraction Interactive Runner ---")
    try:
        arr_input = input("Enter the sorted array (e.g., [1,2,3,5]): ").strip()
        k_input = input("Enter k (e.g., 3): ").strip()
        
        # Safely evaluate inputs
        parsed_arr = ast.literal_eval(arr_input)
        parsed_k = int(k_input)
        
        if not isinstance(parsed_arr, list):
            raise ValueError("Input must be a list of integers.")
            
        # Calling the function
        result = solution.kthSmallestPrimeFraction(parsed_arr, parsed_k)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")