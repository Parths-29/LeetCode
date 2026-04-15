'''
Question: 2515. Shortest Distance to Target String in a Circular Array (Easy)
You are given a 0-indexed circular string array words and a string target. A circular array means that the word's previous element is the last element, and the next element is the first element.
You are also given an integer startIndex. Return the shortest distance needed to reach the string target. If the string does not exist, return -1.

Example 1:
Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.

---
My Approach (Bidirectional Outward Sweep / Modulo Arithmetic):
1. Instead of looping all the way around the circle left, and then all the way right, we can check both directions simultaneously.
2. In a circular array, the furthest distance to any element is exactly half the length of the array (`n // 2`, written as bitwise `n >> 1`).
3. We set up a loop to expand outwards distance `i` from `0` to `n // 2`.
4. We use Python's native handling of negative modulo arithmetic to effortlessly wrap around the ends of the array.
   - Move Right: `(startIndex + i) % n`
   - Move Left: `(startIndex - i) % n`
5. Because we increment `i` starting from 0, the very first time we find the target, it is mathematically guaranteed to be the minimum distance.

Time Complexity: O(N) where N is the length of the words array. We visit at most half the array (checking two elements per iteration).
Space Complexity: O(1) auxiliary space.
'''

import ast
from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        
        # Expand outwards from distance 0 up to half the array length
        for i in range((n >> 1) + 1):
            
            # Check both the forward (right) and backward (left) wrapped indices
            if words[(startIndex + i) % n] == target or words[(startIndex - i) % n] == target:
                return i
                
        return -1

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 2515. Shortest Distance in Circular Array Interactive Runner ---")
    try:
        words_input = input("Enter the words array (e.g., ['hello','i','am','leetcode','hello']): ").strip()
        target_input = input("Enter the target string (e.g., hello): ").strip()
        start_input = input("Enter the startIndex (e.g., 1): ").strip()
        
        # Safely evaluate inputs
        parsed_words = ast.literal_eval(words_input)
        
        # Clean up target string if quotes are accidentally included
        if target_input.startswith(('"', "'")): target_input = target_input[1:-1]
        parsed_start = int(start_input)
            
        result = solution.closestTarget(parsed_words, target_input, parsed_start)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")