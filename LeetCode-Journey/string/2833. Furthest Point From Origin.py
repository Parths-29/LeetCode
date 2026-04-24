'''
Question: 2833. Furthest Point From Origin (Easy)
You are given a string moves of length n consisting only of characters 'L', 'R', and '_'.
The string represents your movement on a number line starting from the origin 0.
- 'L' means move 1 unit left.
- 'R' means move 1 unit right.
- '_' means move 1 unit left or 1 unit right.
Return the maximum distance from the origin you can achieve after executing all moves.

Example 1:
Input: moves = "L_RL__R"
Output: 3
Explanation: The furthest point we can reach from the origin 0 is point 3 through the following moves:
- We lean right: The baseline displacement from given letters is 2 'R's and 2 'L's = 0.
- We have 3 '_' characters. We can greedily make them all 'R's to reach distance 3.

---
My Approach (Greedy / Math Simplification):
1. The problem asks for the absolute maximum distance.
2. The guaranteed 'L' and 'R' moves cancel each other out. Our baseline net displacement from the origin is `abs(R_count - L_count)`.
3. To maximize this distance, we simply assign every single '_' to whichever direction gives us the most distance (the direction we are already leaning).
4. Therefore, the absolute maximum distance is the baseline displacement PLUS the total number of '_' characters available.
5. Pythonic Optimization: Using `.count()` three times leverages Python's underlying C-optimized string methods, which runs exponentially faster than a single-pass manual `for` loop in native Python.

Time Complexity: $O(N)$ where N is the length of the string.
Space Complexity: $O(1)$ auxiliary space.
'''

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Calculate net displacement and greedily add all free choices
        return abs(moves.count("R") - moves.count("L")) + moves.count("_")

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 2833. Furthest Point From Origin Interactive Runner ---")
    try:
        moves_input = input("Enter the moves string (e.g., L_RL__R): ").strip()
        
        # Clean up input if quotes are accidentally pasted
        if moves_input.startswith(('"', "'")): 
            moves_input = moves_input[1:-1]
            
        # Calling the function
        result = solution.furthestDistanceFromOrigin(moves_input)
        print(f"\nMaximum Distance: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")