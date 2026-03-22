'''
Question: 670. Maximum Swap (Medium)
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap is chosen.

---
My Approach (Greedy + Hash Map):
1. A brute force approach would try every single pair of swaps, taking $O(N^2)$ time.
2. We can optimize this to $O(N)$ by being greedy. We want to swap the earliest possible digit with the LARGEST possible digit that appears AFTER it.
3. If there are multiple identical large digits, we want the one that appears LAST (furthest to the right) to maximize the impact of the swap.
4. We build a dictionary `last` that records the last seen index for every digit (0-9).
5. We iterate through the number from left to right. For each digit, we check if there is a larger digit (from 9 down to current_digit + 1) that appears at an index strictly greater than our current index.
6. The absolute second we find one, we make the swap and instantly return the result.

Time Complexity: $O(N)$ where N is the number of digits. The inner loop runs at most 9 times, which is $O(1)$.
Space Complexity: $O(N)$ to store the list of characters and the dictionary.
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of characters for easy manipulation
        num_list = list(str(num))
        
        # Track the last occurrence of each digit (0-9)
        last = {int(d): i for i, d in enumerate(num_list)}
        
        # Traverse the number from left to right
        for i, digit in enumerate(num_list):
            # Check for a larger digit to swap (from 9 down to current digit + 1)
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Swap and return the new number
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(''.join(num_list))
        
        # If no swap occurred, return the original number
        return num

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 670. Maximum Swap Interactive Runner ---")
    try:
        num_input = input("Enter the integer (e.g., 2736): ").strip()
        
        # Safely evaluate input
        num = int(num_input)
            
        # Calling the function
        result = solution.maximumSwap(num)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")