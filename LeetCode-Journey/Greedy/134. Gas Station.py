'''
Question: 134. Gas Station (Medium)
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

---
My Approach:
Greedy Algorithm:
1. First, check if the total sum of `gas` is less than the total sum of `cost`. If it is, it's impossible to complete the circuit, so immediately return -1.
2. Initialize `current_gas` to track the gas in the tank during the current trip, and `start` to track the potential starting station index.
3. Loop through the gas stations. Add the net gas (`gas[i] - cost[i]`) to `current_gas`.
4. If `current_gas` ever drops below 0, it means we can't reach the next station from our current `start` position. 
5. Because of this, any station between our old `start` and our current station `i` is also an invalid starting point. We reset `current_gas` to 0 and set the new potential `start` station to `i + 1`.
6. Since we already proved in Step 1 that a solution definitely exists, the final `start` index left standing is guaranteed to be the correct answer.

Time Complexity: O(N)
Space Complexity: O(1)
'''

import ast
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if it's even mathematically possible to complete the circuit
        if sum(gas) < sum(cost):
            return -1
                
        current_gas = 0
        start = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            
            # If we run out of gas, this starting point (and any point before it) fails
            if current_gas < 0:
                current_gas = 0
                start = i + 1

        return start

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 134. Gas Station Interactive Runner ---")
    try:
        # Responsive input setup for the two arrays
        gas_input = input("Enter the gas array (e.g., [1,2,3,4,5]): ")
        cost_input = input("Enter the cost array (e.g., [3,4,5,1,2]): ")
        
        # Safely evaluate the string inputs into Python lists
        gas = ast.literal_eval(gas_input) 
        cost = ast.literal_eval(cost_input) 
        
        if not isinstance(gas, list) or not isinstance(cost, list):
            raise ValueError("Both inputs must be lists.")
            
        # Calling your function
        result = solution.canCompleteCircuit(gas, cost)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Please make sure you enter valid Python lists. Details: {e}")