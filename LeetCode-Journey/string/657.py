    '''
Question: 657. Robot Return to Origin (Easy)
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Example 1:
Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

Example 2:
Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

---
My Approach (Parity Check + Boolean Arithmetic):
1. Fast Fail (Parity): To return to the origin, every move must have a corresponding counter-move. Thus, a valid sequence MUST have an even length. If the string length is odd (`len(moves) & 1`), we instantly return False.
2. We initialize x and y coordinates to 0.
3. Instead of using slow `if/elif` branches, we use Python's boolean-to-integer conversion. `True` evaluates to 1, and `False` evaluates to 0.
4. `(c == 'U') - (c == 'D')` cleanly translates the vertical axis.
5. `(c == 'R') - (c == 'L')` cleanly translates the horizontal axis.
6. At the end, we simply check if `x` and `y` are both 0 using `not x and not y`.

Time Complexity: $O(N)$ where N is the length of the moves string. We do exactly one pass.
Space Complexity: $O(1)$ auxiliary space.
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Fast fail: impossible to return to origin with an odd number of moves
        if len(moves) & 1: 
            return False
            
        x = y = 0

        # Boolean arithmetic to update coordinates without branching
        for c in moves:
            y += (c == 'U') - (c == 'D')
            x += (c == 'R') - (c == 'L')

        return not x and not y

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 657. Robot Return to Origin Interactive Runner ---")
    try:
        moves_input = input("Enter the moves string (e.g., UDLR): ").strip()
        
        # Clean up input if LeetCode quotes are accidentally pasted
        if moves_input.startswith(('"', "'")): 
            moves_input = moves_input[1:-1]
            
        # Calling the function
        result = solution.judgeCircle(moves_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")