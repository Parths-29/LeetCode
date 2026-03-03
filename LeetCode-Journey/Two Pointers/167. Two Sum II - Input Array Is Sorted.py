'''
Question: 1545. Find Kth Bit in Nth Binary String (Medium)
Given two positive integers n and k, the binary string Sn is formed as follows:
S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1

Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Example 1:
Input: n = 3, k = 1
Output: "0"

Example 2:
Input: n = 4, k = 11
Output: "1"

---
My Approach (Divide and Conquer / Recursion):
1. Notice that the length of the string $S_n$ is always $2^n - 1$.
2. The structure of the string is symmetrical: `[Left Half] + "1" (Middle) + [Right Half]`.
3. The Left Half is exactly $S_{n-1}$.
4. The Right Half is the reverse and inverse of $S_{n-1}$.
5. Instead of building the string, we can track the position of `k` recursively:
   - Base Case: If $n == 1$, the string is just "0", so return "0".
   - Find the middle index: `mid = 2**(n - 1)`.
   - If `k == mid`, the bit is exactly the middle "1", so return "1".
   - If `k < mid`, the bit is in the Left Half, which is identical to $S_{n-1}$. We recurse with `(n-1, k)`.
   - If `k > mid`, the bit is in the Right Half. Because the right half is reversed, its position in $S_{n-1}$ is actually `2**n - k`. Because it's inverted, we must flip the result (e.g., if the recursive call returns "0", we return "1", and vice versa).

Time Complexity: O(N). We make at most N recursive calls, cutting the search space in half each time.
Space Complexity: O(N) due to the recursive call stack depth.
'''

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case
        if n == 1:
            return "0"
            
        length = (1 << n) - 1  # Equivalent to 2^n - 1
        mid = length // 2 + 1  # 1-indexed middle point
        
        if k == mid:
            return "1"
        elif k < mid:
            # It's in the left half, which is identical to S_{n-1}
            return self.findKthBit(n - 1, k)
        else:
            # It's in the right half, which is reversed and inverted
            # Find its mirror position in the left half
            mirror_k = length - k + 1
            res = self.findKthBit(n - 1, mirror_k)
            # Invert the result
            return "1" if res == "0" else "0"

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1545. Find Kth Bit Interactive Runner ---")
    try:
        n_input = input("Enter the integer n (e.g., 4): ")
        k_input = input("Enter the integer k (e.g., 11): ")
        
        n = int(n_input)
        k = int(k_input)
        
        # Calling the function
        result = solution.findKthBit(n, k)
        print(f"\nOutput: '{result}'")
        
    except ValueError:
        print("Error: Please enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")