'''
Question: 473. Matchsticks to Square (Medium)
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

---
My Approach (Backtracking + Reverse Sorting + Symmetry Pruning):
1. Math Check: The total sum of all matchsticks must be perfectly divisible by 4. If not, return False.
2. The target length for each side is `total // 4`.
3. Sort the matchsticks in descending order. Placing the largest elements first guarantees we hit dead ends much faster, aggressively pruning the recursion tree.
4. Backtracking State: Track the current matchstick `index` and an array `sides` of length 4.
5. Elite Optimization (Symmetry Pruning): If we place a matchstick into an empty side (`sides[i] == 0`) and the recursion fails, we immediately `break`. Since all remaining empty sides are mathematically identical, trying them would just waste computation time.

Time Complexity: O(4^N) in the absolute worst case (trying 4 bins for N matchsticks), but practically vastly faster due to descending sort and symmetry pruning.
Space Complexity: O(N) for the recursion stack space.
'''

import ast
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        
        # Fast fail: Perimeter must be divisible by 4
        if total % 4 != 0:
            return False
            
        side = total // 4
        
        # Sort descending to place large, restrictive pieces first
        matchsticks.sort(reverse=True)
        sides = [0, 0, 0, 0]
        n = len(matchsticks)

        def backtrack(index: int) -> bool:
            # Base case: we successfully placed all matchsticks
            if index == n:
                return sides[0] == sides[1] == sides[2] == side
                
            for i in range(4):
                # If the current matchstick fits in this side
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    
                    if backtrack(index + 1):
                        return True
                        
                    # Undo the choice (backtrack)
                    sides[i] -= matchsticks[index]
                    
                # ELITE OPTIMIZATION: Symmetry Pruning
                # If this side was empty and it failed, there's no point
                # trying the next side if it is also empty!
                if sides[i] == 0:
                    break
                    
            return False

        return backtrack(0)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 473. Matchsticks to Square Interactive Runner ---")
    try:
        matchsticks_input = input("Enter the matchsticks array (e.g., [1,1,2,2,2]): ").strip()
        
        # Safely evaluate inputs
        parsed_matchsticks = ast.literal_eval(matchsticks_input)
        
        if not isinstance(parsed_matchsticks, list):
            raise ValueError("Input must be a list of integers.")
            
        # Calling the function
        result = solution.makesquare(parsed_matchsticks)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")