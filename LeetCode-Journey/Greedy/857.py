'''
Question: 857. Minimum Cost to Hire K Workers (Hard)
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.
We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:
1. Every worker in the paid group must be paid at least their minimum wage expectation.
2. In the group, each worker's pay must be directly proportional to their quality. This means if a worker's quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
Return the least amount of money needed to form a paid group satisfying the above conditions.

Example 1:
Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

---
My Approach (Greedy Ratio Sort + Max-Heap):
1. The pay rate for the entire group is bottlenecked by the worker with the highest `wage / quality` ratio.
2. We pair each worker's ratio and quality, and sort them in ascending order of their ratio.
3. As we iterate through the sorted workers, the current worker's ratio will ALWAYS be the maximum ratio in our current selected group.
4. To minimize the formula `cost = current_ratio * total_quality`, we need to keep `total_quality` as low as possible.
5. We use a Max-Heap to keep track of the qualities of the workers in our group. 
6. For every new worker, we add their quality to our sum and push it to the heap. If our group size exceeds `k`, we pop the largest quality out of the heap and subtract it from our sum.
7. Whenever our group size is exactly `k`, we calculate the cost and update our minimum result.

Time Complexity: O(N log N) to sort the workers, plus O(N log K) to process the heap operations. Total is O(N log N).
Space Complexity: O(N) to store the paired workers array and O(K) for the heap. Total is O(N).
'''

import ast
import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Create a list of tuples (ratio, quality) and sort it by ratio ascending
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        
        max_heap = []
        quality_sum = 0
        res = float('inf')
        
        for ratio, q in workers:
            # Python's heapq is a min-heap, so we push negative quality to simulate a max-heap
            heapq.heappush(max_heap, -q)
            quality_sum += q
            
            # If we have more than k workers, kick out the one with the highest quality
            if len(max_heap) > k:
                # Add the popped value (which is negative, so it effectively subtracts)
                quality_sum += heapq.heappop(max_heap)
                
            # Once we have exactly k workers, calculate the cost
            if len(max_heap) == k:
                res = min(res, ratio * quality_sum)
                
        return float(res)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 857. Minimum Cost to Hire K Workers Interactive Runner ---")
    try:
        quality_input = input("Enter the quality array (e.g., [10,20,5]): ").strip()
        wage_input = input("Enter the wage array (e.g., [70,50,30]): ").strip()
        k_input = input("Enter k (e.g., 2): ").strip()
        
        # Safely evaluate inputs
        parsed_quality = ast.literal_eval(quality_input)
        parsed_wage = ast.literal_eval(wage_input)
        parsed_k = int(k_input)
        
        if not isinstance(parsed_quality, list) or not isinstance(parsed_wage, list):
            raise ValueError("quality and wage must be lists of integers.")
            
        # Calling the function
        result = solution.mincostToHireWorkers(parsed_quality, parsed_wage, parsed_k)
        print(f"\nOutput: {result:.5f}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")