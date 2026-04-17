'''
Question: 877. Stone Game (Medium)
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones. The total number of stones across all piles is odd, so there are no ties.
Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row.
Return true if Alice wins the game (assuming both play optimally), or false if Bob wins.

Example 1:
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
If she takes the first 5, the row becomes [3, 4, 5]. Bob takes 5, row becomes [3, 4]. Alice takes 4, Bob takes 3. Alice wins 9 to 8.

---
My Approach (Game Theory / Mathematical Invariant):
1. A standard Dynamic Programming (Minimax) approach takes O(N^2) time, but it's completely unnecessary due to the problem's constraints.
2. The array always has an EVEN number of elements, and the total sum is ODD.
3. Because the elements are even, we can divide them into "Even-indexed" piles and "Odd-indexed" piles.
4. Since the total sum is odd, the sum of Even-indexed piles will NEVER equal the sum of Odd-indexed piles. One will always be strictly larger.
5. Because Alice goes first, she can force the game state. She can choose to ALWAYS take Even-indexed piles, or ALWAYS take Odd-indexed piles. 
6. Since she plays optimally, she will simply choose the parity that holds the larger sum. Bob can never prevent this. Therefore, Alice is mathematically guaranteed to win every single time.

Time Complexity: O(1)
Space Complexity: O(1)
'''

import ast
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # The game is mathematically rigged. Alice always wins.
        return True

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 877. Stone Game Interactive Runner ---")
    try:
        piles_input = input("Enter the piles array (e.g., [5,3,4,5]): ").strip()
        
        # Safely evaluate input
        parsed_piles = ast.literal_eval(piles_input)
        
        if not isinstance(parsed_piles, list):
            raise ValueError("Input must be a valid list of integers.")
            
        result = solution.stoneGame(parsed_piles)
        print(f"\nDoes Alice win? {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")