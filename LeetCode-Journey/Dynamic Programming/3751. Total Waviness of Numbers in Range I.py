''' Question: 3751. Total Waviness of Numbers
You are given two integers, A and B. 
Return the total "waviness" of all numbers in the inclusive range [A, B].
The waviness of a number is the total number of contiguous length-3 subarrays of its digits that strictly form a peak (m > l and m > r) or a valley (m < l and m < r).

---
My Approach (Global DP Precomputation + Prefix Sums):
1. Instead of computing the waviness per query, we precompute the waviness of all numbers up to the maximum limit (100,000) globally.
2. Dynamic Programming State: The waviness of a number `i` is identical to the waviness of `i // 10`, plus 1 if the last three digits of `i` form a valid wave.
3. We maintain a `pref` array to store the cumulative sum of waviness for all numbers from 0 to `i`.
4. When queried for the range [A, B], we simply return `pref[B] - pref[A - 1]`.

Time Complexity: $O(M)$ globally for precomputation (where M is the Max limit), but $O(1)$ per testcase query.
Space Complexity: $O(M)$ auxiliary space to store the DP and Prefix arrays in memory.
'''

import ast

class Solution:
    # 1. Global Precomputation: Runs exactly once when the module loads
    Max = 100001
    dp = [0] * Max
    pref = [0] * Max

    for i in range(100, Max):
        # Extract the last three digits: Left (l), Middle (m), Right (r)
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10

        # A wave is a strict local maximum (peak) or strict local minimum (valley)
        isWave = (m > max(l, r)) or (m < min(l, r))
        
        # Inherit the waves from the prefix of the number, plus the new wave (if any)
        dp[i] = dp[i // 10] + int(isWave)
        
        # Build the prefix sum array for O(1) range queries
        pref[i] = pref[i - 1] + dp[i]

    def totalWaviness(self, A: int, B: int) -> int:
        # 2. O(1) Range Query Resolution
        return self.pref[B] - self.pref[A - 1]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3751. Total Waviness of Numbers Interactive Runner ---")
    try:
        a_input = input("Enter lower bound A (e.g., 100): ").strip()
        b_input = input("Enter upper bound B (e.g., 1000): ").strip()
        
        # Safely evaluate inputs
        parsed_A = int(a_input)
        parsed_B = int(b_input)
            
        result = solution.totalWaviness(parsed_A, parsed_B)
        print(f"\nTotal Waviness in range [{parsed_A}, {parsed_B}]: {result}")
        
    except ValueError as ve:
        print("Error: Inputs must be valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

