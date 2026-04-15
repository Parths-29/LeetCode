'''
Question: 3222. Find the Winning Player in Coin Game (Easy)
You are given two positive integers x and y, denoting the number of coins with values 75 and 10 respectively.
Alice and Bob are playing a game. Each turn, starting with Alice, the player must pick up coins with a total value 115. If the player is unable to do so, they lose the game.
Return the name of the player who wins the game if both players play optimally.

Example 1:
Input: x = 2, y = 7
Output: "Alice"
Explanation: The game ends in a single turn:
Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.

---
My Approach (Game Theory / Math Simplification):
1. To make a total value of 115 using 75 and 10, the ONLY mathematical possibility is exactly one 75-coin and four 10-coins. (1*75 + 4*10 = 115).
2. Because there is no branching strategy, the total number of turns in the game is fixed from the very beginning. 
3. The game will last exactly `min(x, y // 4)` turns.
4. Since Alice goes first, an odd number of total turns means Alice makes the last move and wins. An even number means Bob wins.
5. We calculate `turns % 2` to get either 1 (Alice) or 0 (Bob), and use it to instantly index into the array `['Bob', 'Alice']`.

Time Complexity: O(1) mathematical calculation.
Space Complexity: O(1) auxiliary space.
'''

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        # Array indexing: 0 resolves to 'Bob' (Even turns), 1 resolves to 'Alice' (Odd turns)
        return ['Bob', 'Alice'][min(x, y // 4) % 2]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3222. Winning Player in Coin Game Interactive Runner ---")
    try:
        x_input = input("Enter the number of 75-value coins (x): ").strip()
        y_input = input("Enter the number of 10-value coins (y): ").strip()
        
        # Safely evaluate inputs
        parsed_x = int(x_input)
        parsed_y = int(y_input)
            
        result = solution.winningPlayer(parsed_x, parsed_y)
        print(f"\nWinner: {result}")
        
    except ValueError:
        print("Error: Inputs must be valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")