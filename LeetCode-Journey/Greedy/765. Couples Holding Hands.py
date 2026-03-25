'''
Question: 765. Couples Holding Hands (Hard)
n couples sit in 2n seats arranged in a row and want to hold hands.
The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat.
The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on.
Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

Example 1:
Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

---
My Approach (Greedy + Hash Map + Bitwise XOR):
1. The mathematical relationship between couples is perfectly captured by a bitwise XOR: a person's partner is always `person ^ 1`.
2. Instead of using `row.index()` which takes O(N) time and makes the overall algorithm O(N^2), we pre-compute a dictionary `pos` that maps each person's ID to their current index.
3. We iterate through the row in steps of 2 (looking at pairs of seats).
4. For the person in the left seat (`row[i]`), we calculate who their partner should be.
5. If the person in the right seat (`row[i+1]`) is NOT the partner, a swap is required.
6. We use our `pos` map to instantly find where the actual partner is sitting.
7. We swap the wrong person and the partner in the `row` array, and crucially, we update the `pos` map to reflect their new seats!

Time Complexity: O(N) where N is the length of the row. We do a single pass to build the map, and a single pass to check/swap.
Space Complexity: O(N) to store the positions in a hash map.
'''

import ast
from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # Create a map of person_id -> current_index for O(1) lookups
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        
        for i in range(0, len(row), 2):
            first_person = row[i]
            partner = first_person ^ 1
            
            # If the person next to them isn't their rightful partner
            if row[i + 1] != partner:
                swaps += 1
                
                # Find where the partner is actually sitting
                partner_idx = pos[partner]
                
                # Identify the wrong person currently sitting next to first_person
                wrong_person = row[i + 1]
                
                # Swap them in the row array
                row[i + 1], row[partner_idx] = row[partner_idx], row[i + 1]
                
                # Update the positions map to reflect the swap
                pos[wrong_person] = partner_idx
                pos[partner] = i + 1
                
        return swaps

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 765. Couples Holding Hands Interactive Runner ---")
    try:
        row_input = input("Enter the row array (e.g., [0,2,1,3]): ").strip()
        
        # Safely evaluate input
        parsed_row = ast.literal_eval(row_input)
        
        if not isinstance(parsed_row, list):
            raise ValueError("Input must be a list of integers.")
            
        # Calling the function
        result = solution.minSwapsCouples(parsed_row)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")