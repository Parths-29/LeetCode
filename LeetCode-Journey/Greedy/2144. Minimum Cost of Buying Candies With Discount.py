'''
Question: 2144. Minimum Cost of Buying Candies With Discount (Easy)
A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.
The customer can choose any candy to take for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.
Return the minimum cost of buying all the candies.

---
My Approach (Greedy + Pythonic Slicing):
1. To maximize our savings, we want the "free" candies to be as expensive as possible. 
2. We sort the candies in descending order so we are always grouping the most expensive ones together.
3. Once sorted descending, the free candies will always be at indices 2, 5, 8, etc.
4. Instead of writing slow Python `for` loops with modulo arithmetic, we use Python's built-in array slicing `cost[2::3]` to extract all the free candies in highly-optimized C-code.
5. The total minimum cost is simply the total sum of all candies MINUS the sum of the free candies.

Time Complexity: O(N log N) dominated by the sorting step. The slicing and summation are strictly O(N).
Space Complexity: O(1) auxiliary space (Python's slice and sum do not require heavy memory allocations here).
'''

import ast
from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        # Sum of all candies minus the sum of every 3rd candy (the free ones)
        return sum(cost) - sum(cost[2::3])

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 2144. Min Cost of Buying Candies (Slicing Trick) ---")
    try:
        cost_input = input("Enter the cost array (e.g., [6, 5, 7, 9, 2, 2]): ").strip()
        
        # Safely evaluate input
        parsed_cost = ast.literal_eval(cost_input)
        
        if not isinstance(parsed_cost, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.minimumCost(parsed_cost)
        print(f"\nMinimum cost to buy all candies: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")