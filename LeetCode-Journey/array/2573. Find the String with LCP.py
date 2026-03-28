'''
Question: 2573. Find the String with LCP (Hard)
We define the LCP matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:
lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i..n-1] and word[j..n-1].
Given an n x n matrix lcp, return the lexicographically smallest string word that corresponds to lcp. If there is no such string, return an empty string.

Example 1:
Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
Output: "abab"
Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".

---
My Approach (Greedy Assignment + In-Place DP Validation):
1. Instead of using a Disjoint Set Union (DSU) to group identical characters, we can do it greedily.
2. We initialize an empty word array of size `n`.
3. Forward Pass (Assignment): We iterate `i` from 0 to n-1. 
   - If `word[i]` is empty, we assign it the smallest available unused character (starting at 'a'). If we run out of the 26 alphabet characters, it's invalid (return "").
   - We then scan all `j` > `i`. If `lcp[i][j] > 0`, it means `word[j]` MUST perfectly match `word[i]`. We assign it. If `word[j]` was already assigned something else, the matrix is contradictory (return "").
4. Backward Pass (Validation): Just because we assigned characters doesn't mean the original matrix was valid. We iterate backwards and dynamically calculate what the LCP *should* be based on our new string.
   - If `word[i] == word[j]`, the expected LCP is `1 + lcp[i+1][j+1]`.
   - If `word[i] != word[j]`, the expected LCP is `0`.
   - If the original `lcp[i][j]` doesn't perfectly match our expected value at any point, the matrix is mathematically impossible. Return "".

Time Complexity: O(N^2) where N is the length of the LCP matrix. We do one O(N^2) pass for assignment and one for validation.
Space Complexity: O(N) auxiliary space to store the generated string characters. We completely avoid building a secondary N x N DP matrix.
'''

import ast
from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n
        current_char = 'a'
        
        # Step 1: Greedily assign characters
        for i in range(n):
            if not word[i]:
                # If we exceed 'z', we can't form a valid lowercase string
                if current_char > 'z':
                    return ""
                word[i] = current_char
                current_char = chr(ord(current_char) + 1)
            
            # Immediately enforce the LCP rules for all future characters
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    if not word[j]:
                        word[j] = word[i]
                    elif word[j] != word[i]:
                        # Contradiction: LCP says they should be equal, but they were already assigned different chars
                        return ""
                        
        # Step 2: Validate the matrix mathematically backwards
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected_lcp = 0
                if word[i] == word[j]:
                    expected_lcp = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                
                # If the given matrix doesn't match reality, it's invalid
                if lcp[i][j] != expected_lcp:
                    return ""
                    
        return "".join(word)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 2573. Find the String with LCP Interactive Runner ---")
    try:
        lcp_input = input("Enter the LCP matrix (e.g., [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]): ")
        
        # Safely evaluate inputs
        parsed_lcp = ast.literal_eval(lcp_input)
        
        if not isinstance(parsed_lcp, list) or (parsed_lcp and not isinstance(parsed_lcp[0], list)):
            raise ValueError("Input must be a 2D list of integers.")
            
        # Calling the function
        result = solution.findTheString(parsed_lcp)
        print(f"\nOutput: \"{result}\"")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")