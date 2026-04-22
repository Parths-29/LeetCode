'''
Question: 2452. Words Within Two Edits of Dictionary (Medium)
You are given two string arrays, queries and dictionary. All words in each array comprise lowercase English letters and have the same length.
For each query in queries, you can form a word from the dictionary if you can change at most two characters in the query.
Return an array of all queries that can form a word from the dictionary.

Example 1:
Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation:
- "word" matches "wood" with 1 edit ('r' -> 'o').
- "note" matches "joke" with 2 edits ('n' -> 'j', 't' -> 'k').
- "ants" cannot match any dictionary word within 2 edits.
- "wood" matches "wood" with 0 edits.

---
My Approach (Early-Exit Search + Pythonic List Comprehensions):
1. The brute-force check is $O(Q \times D \times N)$, which is fast enough for the constraints, but we can heavily optimize the constant factors.
2. We define a helper function `is_match(q, d)` that compares two words character by character using `zip()`.
3. Spatial Pruning: We track differences. The exact moment we hit 3 differences, we instantly return `False` to avoid checking the rest of the string.
4. Functional Short-Circuiting: We use a list comprehension combined with Python's `any()` function. `any()` acts as an automatic `break` statement; it stops evaluating the dictionary the second it finds a valid match for the query.

Time Complexity: $O(Q \times D \times N)$ worst case, where Q is queries length, D is dictionary length, and N is word length. With early exits, average time is drastically lower.
Space Complexity: $O(1)$ auxiliary space (excluding the output array).
'''

import ast
from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        # Helper function to check if two words are within 2 edits
        def is_match(q: str, d: str) -> bool:
            diffs = 0
            # zip() pairs characters up efficiently
            for c1, c2 in zip(q, d):
                if c1 != c2:
                    diffs += 1
                    # Spatial early exit: more than 2 edits makes it invalid
                    if diffs > 2:
                        return False
            return True

        # Pythonic one-liner: any() handles the early exit 'break' automatically
        return [q for q in queries if any(is_match(q, d) for d in dictionary)]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 2452. Words Within Two Edits of Dictionary Interactive Runner ---")
    try:
        queries_input = input("Enter the queries array (e.g., ['word','note','ants','wood']): ").strip()
        dict_input = input("Enter the dictionary array (e.g., ['wood','joke','moat']): ").strip()
        
        # Safely evaluate inputs
        parsed_queries = ast.literal_eval(queries_input)
        parsed_dict = ast.literal_eval(dict_input)
        
        if not isinstance(parsed_queries, list) or not isinstance(parsed_dict, list):
            raise ValueError("Inputs must be valid lists of strings.")
            
        result = solution.twoEditWords(parsed_queries, parsed_dict)
        print(f"\nValid Queries: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")