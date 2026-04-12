'''
Question: 1320. Minimum Distance to Type a Word Using Two Fingers (Hard)
You have a keyboard layout of 26 English lowercase letters in a 5x6 grid.
Given a string word, return the minimum total distance to type such string using only two fingers.

---
My Approach (1D Dynamic Programming State Compression):
1. Since we must type the characters in order, after typing `word[i]`, one finger is MATHEMATICALLY GUARANTEED to be resting on `word[i]`.
2. Therefore, our DP state only needs to track the position of the *other* finger!
3. We use a dictionary `dp` where the key is the position of the other finger, and the value is the minimum cost. '26' represents the initial hovering state.
4. For each new character `curr`, we calculate two choices for every existing state:
   - Move the finger currently on `prev` to `curr`. (The other finger stays where it is).
   - Move the `other_finger` to `curr`. (The finger on `prev` stays behind and becomes the NEW other finger).
5. This reduces the space complexity from O(N * 26) to O(1) constant space!

Time Complexity: O(N * 26) -> O(N) where N is the length of the word.
Space Complexity: O(26) -> O(1) auxiliary space.
'''

class Solution:
    def minimumDistance(self, word: str) -> int:
        # Helper to calculate Manhattan distance on the 5x6 keyboard
        def dist(p1: int, p2: int) -> int:
            if p1 == 26 or p2 == 26: 
                return 0  # 26 represents hovering (0 cost to drop)
            return abs(p1 // 6 - p2 // 6) + abs(p1 % 6 - p2 % 6)
            
        # dp stores {position_of_other_finger : min_cost}
        dp = {26: 0} 
        prev = ord(word[0]) - 65
        
        for c in word[1:]:
            curr = ord(c) - 65
            new_dp = {}
            
            for other_finger, cost in dp.items():
                # Choice 1: Move the 'prev' finger to 'curr'
                cost1 = cost + dist(prev, curr)
                new_dp[other_finger] = min(new_dp.get(other_finger, float('inf')), cost1)
                
                # Choice 2: Move the 'other_finger' to 'curr'
                cost2 = cost + dist(other_finger, curr)
                new_dp[prev] = min(new_dp.get(prev, float('inf')), cost2)
                
            dp = new_dp
            prev = curr
            
        return min(dp.values())

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 1320. Minimum Distance to Type a Word Interactive Runner ---")
    try:
        word_input = input("Enter the word (e.g., CAKE): ").strip()
        if word_input.startswith(('"', "'")): word_input = word_input[1:-1]
        
        result = solution.minimumDistance(word_input.upper())
        print(f"\nOutput: {result}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")