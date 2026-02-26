'''
Question: 621. Task Scheduler (Medium)
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in 
any order, but there's a constraint: there has to be a gap of at least n intervals between 
two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

---
My Approach (Math / Greedy):
1. Count the frequencies of all tasks. 
2. Find the maximum frequency among all tasks (`max_freq`).
3. The most frequent task dictates the "framework" of our schedule. We arrange them with `n` empty slots between them.
   The number of "chunks" or gaps between these max-frequency tasks is `(max_freq - 1)`.
   The length of each chunk (including the task itself and the idle slots) is `(n + 1)`.
4. So, the base length of our schedule is `(max_freq - 1) * (n + 1)`.
5. Finally, we add the number of tasks that share this same `max_freq` (because they will sit at the very end of the schedule).
6. Edge case: If `n` is very small or there are many distinct tasks, we might not need any idle time at all. In that case, the answer is just the length of the `tasks` array. We return the maximum of our calculated intervals and `len(tasks)`.

Time Complexity: O(N) where N is the total number of tasks.
Space Complexity: O(1) (array of size 26 for frequencies)
'''

import ast
import collections
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1 & 2: Get frequencies and the maximum frequency
        task_counts = collections.Counter(tasks)
        max_freq = max(task_counts.values())
        
        # Step 3: Count how many tasks have this exact maximum frequency
        max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Step 4 & 5: Calculate the required intervals
        intervals = (max_freq - 1) * (n + 1) + max_freq_count
        
        # Step 6: Return the max of calculated intervals and the total number of tasks
        return max(len(tasks), intervals)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 621. Task Scheduler Interactive Runner ---")
    try:
        # Responsive input setup for list of strings and an integer
        tasks_input = input("Enter the tasks array (e.g., ['A','A','A','B','B','B']): ")
        n_input = input("Enter the value of n (e.g., 2): ")
        
        # Safely evaluate the inputs
        tasks = ast.literal_eval(tasks_input) 
        n = int(n_input)
        
        if not isinstance(tasks, list):
            raise ValueError("Tasks input must be a list.")
            
        # Calling the function
        result = solution.leastInterval(tasks, n)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")