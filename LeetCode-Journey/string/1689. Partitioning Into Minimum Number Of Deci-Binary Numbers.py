'''
Question: 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers (Medium)
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Example 1:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:
Input: n = "82734"
Output: 8

Example 3:
Input: n = "27346209830709182346"
Output: 9

---
My Approach (Greedy / Math Observation):
1. A deci-binary number consists of only 0s and 1s.
2. If we stack deci-binary numbers and add them together, each number can only add a maximum of 1 to any digit's place.
3. Therefore, to reach a specific digit `d` in any column, we must add exactly `d` ones together.
4. The maximum digit in the entire string `n` will dictate the absolute minimum number of deci-binary numbers we need to stack.
5. So, the solution is simply finding the maximum character in the string `n` and converting it to an integer.

Time Complexity: O(N) where N is the length of the string `n` (to scan for the max digit).
Space Complexity: O(1)
'''

class Solution:
    def minPartitions(self, n: str) -> int:
        # Find the maximum character in the string and convert it to an integer
        return int(max(n))

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1689. Min Deci-Binary Partitions Interactive Runner ---")
    try:
        # Responsive input setup for string
        user_input = input("Enter the number string n (e.g., 82734): ").strip()
        
        # Clean up input if the user accidentally pastes quotes
        if user_input.startswith(('"', "'")) and user_input.endswith(('"', "'")):
            user_input = user_input[1:-1]
            
        if not user_input.isdigit():
            raise ValueError("Input must be a valid positive integer string.")
            
        # Calling the function
        result = solution.minPartitions(user_input)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")