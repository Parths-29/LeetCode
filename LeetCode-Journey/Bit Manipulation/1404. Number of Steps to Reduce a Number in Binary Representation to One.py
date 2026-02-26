'''
Question: 1404. Number of Steps to Reduce a Number in Binary Representation to One (Medium)
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
- If the current number is even, you have to divide it by 2.
- If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.

---
My Approach (Right-to-Left Bit Simulation):
1. Instead of converting the string to an integer, iterate backward through the string starting from the last character down to index 1.
2. Keep track of the number of `steps` and a `carry` (which represents adding 1).
3. At each step, calculate the effective bit: `int(s[i]) + carry`.
4. If the effective bit is 1 (Odd): We have to add 1 (takes 1 step) which makes it even, and then divide by 2 (takes 1 step). Total = 2 steps. We also set `carry = 1`.
5. If the effective bit is 0 or 2 (Even): We just divide by 2 (takes 1 step). The carry remains whatever it was.
6. Finally, add any remaining `carry` to the total steps (this accounts for the very first bit flipping from '1' to '10').

Time Complexity: O(N) where N is the length of the string.
Space Complexity: O(1)
'''

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Iterate from the last bit down to the second bit (index 1)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry
            
            if bit == 1:
                # Odd: Add 1 (1 step) + Divide by 2 (1 step) = 2 steps
                carry = 1
                steps += 2
            else:
                # Even: Divide by 2 (1 step)
                steps += 1
                
        # If there's a carry left for the most significant bit, add 1 step
        return steps + carry

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1404. Number of Steps Interactive Runner ---")
    try:
        # Responsive input setup for string
        # No need for ast.literal_eval here since the input is just a string!
        user_input = input("Enter the binary string (e.g., 1101): ").strip()
        
        # Clean up input if the user accidentally pastes quotes
        if user_input.startswith(('"', "'")) and user_input.endswith(('"', "'")):
            user_input = user_input[1:-1]
            
        if not user_input:
            raise ValueError("Input cannot be empty.")
            
        # Calling the function
        result = solution.numSteps(user_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")