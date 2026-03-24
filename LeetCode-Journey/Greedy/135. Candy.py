'''
Question: 135. Candy (Hard)
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

---
My Approach (Two-Pass Greedy Algorithm):
1. Initialize a `candies` array of size `n` with 1s, satisfying the rule that every child gets at least one candy.
2. First Pass (Left to Right): Iterate from index 1 to n-1. If `ratings[i] > ratings[i-1]`, update `candies[i] = candies[i-1] + 1`. This ensures higher-rated children have more candy than their LEFT neighbor.
3. Second Pass (Right to Left): Iterate from index n-2 down to 0. If `ratings[i] > ratings[i+1]`, update `candies[i] = max(candies[i], candies[i+1] + 1)`. 
   - We use `max()` to ensure we don't accidentally reduce the candy count of a child who already needed a lot of candies to satisfy their left neighbor.
4. The total minimum candies required is simply the sum of the `candies` array.

Time Complexity: $O(N)$ where N is the number of children. We iterate through the array exactly twice.
Space Complexity: $O(N)$ to store the candies array.
'''

import ast
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # Pass 1: Compare with the left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        # Pass 2: Compare with the right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Take the max so we don't invalidate the left-to-right pass
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        return sum(candies)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 135. Candy Interactive Runner ---")
    try:
        ratings_input = input("Enter the ratings array (e.g., [1,0,2]): ").strip()
        
        # Safely evaluate input
        parsed_ratings = ast.literal_eval(ratings_input)
        
        if not isinstance(parsed_ratings, list):
            raise ValueError("Input must be a list of integers.")
            
        # Calling the function
        result = solution.candy(parsed_ratings)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")