'''
Question: 126. Word Ladder II (Hard)
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList.
- sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

---
My Approach (Level-Order BFS + Path Tracking + Deferred Deletion):
1. We use a Hash Set `wordSet` for $O(1)$ lookups.
2. We create a generator `neighbors` that finds all valid adjacent words by swapping each character with all 26 lowercase letters. This is vastly faster than scanning the entire dictionary.
3. We use a dictionary `level` to track the current layer of the BFS. The keys are the current words, and the values are lists of all paths taken to reach that word.
4. As we build `nextLevel`, we append valid neighbors to the existing paths.
5. If we hit the `endWord`, we immediately return the paths, because BFS guarantees we have found the absolute shortest routes.
6. Crucial Step: We remove visited words from `wordSet` ONLY at the end of the level (`wordSet -= set(nextLevel.keys())`). This allows multiple different shortest paths to converge on the same word in the same layer without blocking each other.

Time Complexity: $O(N \times 26 \times L)$ where N is the number of words and L is the length of the word.
Space Complexity: $O(N \times P)$ where P is the number of paths stored in the worst-case BFS branching.
'''

import ast
import string
from collections import defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        wordSet.discard(beginWord)

        # Generator to find valid adjacent words in O(26 * L) time
        def neighbors(word):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        yield newWord

        # level tracks {current_word: [[path1], [path2], ...]}
        level = {beginWord: [[beginWord]]}
        
        while level:
            nextLevel = defaultdict(list)
            for word, paths in level.items():
                
                # First time we see endWord, we are guaranteed it's the shortest path
                if word == endWord:
                    return paths
                    
                for nei in neighbors(word):
                    for path in paths:
                        nextLevel[nei].append(path + [nei])
                        
            # Deferred deletion: Remove visited words after the entire level is processed
            # This allows multiple paths to share the same intermediate word
            wordSet -= set(nextLevel.keys())
            level = nextLevel

        return []

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 126. Word Ladder II Interactive Runner ---")
    try:
        begin_input = input("Enter beginWord (e.g., hit): ").strip()
        end_input = input("Enter endWord (e.g., cog): ").strip()
        list_input = input("Enter wordList (e.g., ['hot','dot','dog','lot','log','cog']): ").strip()
        
        # Clean quotes
        if begin_input.startswith(('"', "'")): begin_input = begin_input[1:-1]
        if end_input.startswith(('"', "'")): end_input = end_input[1:-1]
        
        # Safely evaluate inputs
        parsed_list = ast.literal_eval(list_input)
        
        if not isinstance(parsed_list, list):
            raise ValueError("wordList must be a valid list of strings.")
            
        result = solution.findLadders(begin_input, end_input, parsed_list)
        
        print("\nShortest Paths:")
        if not result:
            print("[] (No valid paths found)")
        for path in result:
            print(path)
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")