'''
Question: 1025. Divisor Game (Easy)
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
- Choosing any x with 0 < x < n and n % x == 0.
- Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:
Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

---
My Approach (Game Theory / Mathematical Parity):
1. A standard DP approach takes O(N^2) time, but we can solve this in O(1) by analyzing the parity (Even/Odd) of the game states.
2. The losing state is n = 1 (an Odd number).
3. If a player receives an Odd number, any valid divisor MUST be Odd. Odd - Odd = Even. Therefore, a player with an Odd number is forced to give their opponent an Even number.
4. If a player receives an Even number, they can always choose the divisor 1. Even - 1 = Odd. Therefore, they can always force their opponent to receive an Odd number.
5. Since Alice plays first, if she starts with an Even number, she can permanently trap Bob in the Odd state until he reaches 1 and loses. If she starts with an Odd number, Bob will trap her.

Time Complexity: O(1) constant time mathematical check.
Space Complexity: O(1) auxiliary space.
'''

import ast

class Solution:
    def divisorGame(self, n: int) -> bool:
        # If n is even, Alice can perfectly control the game and win.
        return n % 2 == 0

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 1025. Divisor Game Interactive Runner ---")
    try:
        n_input = input("Enter the starting number n (e.g., 2): ").strip()
        
        # Safely evaluate input
        parsed_n = int(n_input)
            
        result = solution.divisorGame(parsed_n)
        print(f"\nDoes Alice win? {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")