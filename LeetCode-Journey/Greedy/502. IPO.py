'''
Question: 502. IPO (Hard)
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

Example 1:
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

---
My Approach (Greedy + Max-Heap):
1. Zip the `capital` and `profits` arrays together into a list of tuples: `(capital, profit)`.
2. Sort this list of projects in ascending order based on their capital requirements.
3. Initialize a Max-Heap (using Python's `heapq` with negative values) to keep track of the highest available profits.
4. Iterate `k` times (since we can pick at most `k` projects):
   - While we still have projects in our sorted list and the cheapest project's capital requirement is less than or equal to our current capital `w`, pop that project from the list and push its profit into the Max-Heap.
   - If the Max-Heap is empty, it means we can't afford any of the remaining projects, so we break out of the loop early.
   - Pop the maximum profit from the Max-Heap (remembering to negate it back to positive) and add it to `w`.
5. Return the final accumulated capital `w`.

Time Complexity: $O(N \\log N + K \\log N)$ where N is the number of projects. Sorting takes $O(N \\log N)$, and we push/pop from the heap at most N and K times.
Space Complexity: $O(N)$ to store the zipped list of projects and the heap.
'''

import ast
import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Step 1 & 2: Zip and sort projects by capital required
        projects = list(zip(capital, profits))
        projects.sort()
        
        max_heap = []
        ptr = 0
        n = len(projects)
        
        # Step 4: Pick up to k projects
        for _ in range(k):
            # Push all affordable projects into the max heap
            while ptr < n and projects[ptr][0] <= w:
                # Multiply profit by -1 to simulate a Max-Heap using Python's Min-Heap
                heapq.heappush(max_heap, -projects[ptr][1])
                ptr += 1
            
            # If we can't afford any more projects, break early
            if not max_heap:
                break
                
            # Pop the max profit, multiply by -1 to make it positive, and add to capital
            w += -heapq.heappop(max_heap)
            
        return w

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 502. IPO Interactive Runner ---")
    try:
        k_input = input("Enter max projects k (e.g., 2): ")
        w_input = input("Enter initial capital w (e.g., 0): ")
        profits_input = input("Enter profits array (e.g., [1,2,3]): ")
        capital_input = input("Enter capital array (e.g., [0,1,1]): ")
        
        # Safely evaluate inputs
        k = int(k_input)
        w = int(w_input)
        parsed_profits = ast.literal_eval(profits_input)
        parsed_capital = ast.literal_eval(capital_input)
        
        if not isinstance(parsed_profits, list) or not isinstance(parsed_capital, list):
            raise ValueError("Profits and capital inputs must be lists.")
            
        # Calling the function
        result = solution.findMaximizedCapital(k, w, parsed_profits, parsed_capital)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")