'''
Question: 292. Nim Game (Easy)
You are playing the following Nim Game with your friend:
- Initially, there is a heap of stones on the table.
- You and your friend will alternate turns, and you go first.
- On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
- The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

Example 1:
Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes 1 stone, including the last stone. Your friend wins.
In all outcomes, your friend wins.

---
My Approach (Game Theory / Math):
1. This is a classic combinatorial game. 
2. If the number of stones is exactly 4, whoever moves first is guaranteed to lose because they must leave 1, 2, or 3 stones, allowing the second player to take the rest.
3. By induction, if the starting number of stones is any multiple of 4 (4, 8, 12, etc.), the second player can always guarantee a win by simply making sure the total stones taken in each round (Player 1 + Player 2) equals exactly 4.
4. Therefore, if `n` is perfectly divisible by 4, you lose. If it is not, you can take `n % 4` stones on your first turn, forcing your opponent into the losing multiple-of-4 state.

Time Complexity: O(1) mathematical calculation.
Space Complexity: O(1) auxiliary space.
'''

class Solution:
    def canWinNim(self, n: int) -> bool:
        # If n is a multiple of 4, you are forced into a losing state.
        return n % 4 != 0

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 292. Nim Game Interactive Runner ---")
    try:
        n_input = input("Enter the number of stones n (e.g., 4): ").strip()
        
        # Safely evaluate input
        n = int(n_input)
            
        # Calling the function
        result = solution.canWinNim(n)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")