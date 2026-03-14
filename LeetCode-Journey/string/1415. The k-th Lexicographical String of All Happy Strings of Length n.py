'''
Question: 1415. The k-th Lexicographical String of All Happy Strings of Length n (Medium)
A happy string is a string that consists only of letters of the set ['a', 'b', 'c'] and s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (1-indexed).
Given two integers n and k, return the k-th lexicographical string of all happy strings of length n. 
Return an empty string if there are less than k happy strings of length n.

Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The 3rd string is "c".

Example 2:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3. The 9th string is "cab".

---
My Approach (Combinatorics / Math):
1. Calculate the absolute maximum number of happy strings: `3 * 2^(n-1)`.
2. If `k` is strictly greater than this total, it's impossible, so return an empty string immediately.
3. Convert `k` to be 0-indexed (`k -= 1`) to make the math line up perfectly.
4. For the first character, the array is split into 3 massive blocks (starting with 'a', 'b', or 'c'). Find which block `k` falls into by dividing by `2^(n-1)`.
5. For all subsequent characters, the array of remaining options is split into 2 blocks. We filter out the previously chosen character, find the new index (`0` or `1`), and append the choice.
6. Shrink `k` using the modulo operator to find its position in the next subset.

Time Complexity: O(n) where n is the length of the string. We literally just calculate the characters one by one.
Space Complexity: O(n) to store the characters of our result before joining them into a string.
'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Calculate total possible happy strings
        total_strings = 3 * (1 << (n - 1))
        
        # If k is out of bounds, return empty
        if k > total_strings:
            return ""
            
        k -= 1  # Make k 0-indexed for the math
        choices = ['a', 'b', 'c']
        
        # 1. Handle the first character (3 choices)
        block_size = 1 << (n - 1)
        first_char_idx = k // block_size
        res = [choices[first_char_idx]]
        k %= block_size
        
        # 2. Handle the remaining characters (2 choices each)
        for i in range(n - 2, -1, -1):
            block_size = 1 << i
            next_char_idx = k // block_size
            
            # Available choices are the original choices minus the last used character
            available_choices = [c for c in choices if c != res[-1]]
            res.append(available_choices[next_char_idx])
            
            # Update k to point relative to the new block
            k %= block_size
            
        return "".join(res)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 1415. The k-th Happy String Interactive Runner ---")
    try:
        n_input = input("Enter the length n (e.g., 3): ").strip()
        k_input = input("Enter the integer k (e.g., 9): ").strip()
        
        n = int(n_input)
        k = int(k_input)
            
        # Calling the function
        result = solution.getHappyString(n, k)
        print(f"\nOutput: '{result}'")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")