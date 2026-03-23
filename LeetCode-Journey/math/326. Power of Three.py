'''
Question: 319. Bulb Switcher (Medium)
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
Return the number of bulbs that are on after n rounds.

Example 1:
Input: n = 3
Output: 1
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 
So you should return 1, because there is only one bulb is on.

Example 2:
Input: n = 0
Output: 0

---
My Approach (Math / Number Theory):
1. A bulb at index `i` is toggled once for every factor it has.
2. A bulb will remain ON at the end only if it was toggled an ODD number of times.
3. Factors mathematically come in pairs (e.g., 2 * 6 = 12). The ONLY numbers that have an odd number of factors are perfect squares (e.g., 6 * 6 = 36, where the factor 6 only counts once).
4. Therefore, the bulbs that remain ON are exactly the bulbs whose indices are perfect squares (1, 4, 9, 16, 25...).
5. The number of perfect squares less than or equal to `n` is exactly the square root of `n`, rounded down to the nearest integer.

Time Complexity: O(1) as calculating the square root is a constant time mathematical operation.
Space Complexity: O(1) auxiliary space.
'''

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # The number of perfect squares up to n is simply floor(sqrt(n))
        return int(n ** 0.5)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 319. Bulb Switcher Interactive Runner ---")
    try:
        n_input = input("Enter the number of bulbs n (e.g., 3): ").strip()
        
        # Safely evaluate input
        n = int(n_input)
        
        if n < 0:
            raise ValueError("Number of bulbs cannot be negative.")
            
        # Calling the function
        result = solution.bulbSwitch(n)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")