'''
Question: 3464. Maximize the Distance Between Points on a Square (Hard)
You are given an integer side denoting the side length of a square placed on a 2D plane with its corners at (0, 0), (0, side), (side, side), and (side, 0).
You are also given a 2D integer array points where points[i] = [xi, yi] represents a point strictly on the boundary of the square.
You need to select exactly k points such that the minimum distance between any two selected points (measured along the perimeter of the square) is maximized.
Return the maximum possible minimum distance.

---
My Approach (1D Perimeter Unrolling + Binary Search on Answer + Sliding Pointers):
1. 2D to 1D Mapping: The distance between points on a square's boundary is just their distance along the perimeter. We "unroll" the square into a 1D line of length `4 * side`.
   - Left edge (x=0): distance is y
   - Top edge (y=side): distance is side + x
   - Right edge (x=side): distance is 3*side - y
   - Bottom edge (y=0): distance is 4*side - x
2. We sort these 1D distances. The problem is now: "Choose k elements from a circular sorted array such that the minimum gap is maximized."
3. We binary search the answer `mid`.
4. The Validation `check(n)`: We greedily try to place `k` points with at least `n` distance. 
5. Because the array is circular, starting at `res[0]` might not be optimal. If the first greedy pass fails, we shift our starting point forward. Instead of recalculating from scratch, we efficiently nudge our existing $K$ pointers forward, ensuring the validation runs in amortized O(N) time!

Time Complexity: $O(N \log N + N \log(\text{Max\_Distance}))$ where N is the number of points. Sorting takes $O(N \log N)$, and binary searching the answer takes $\log(\text{Max\_Distance})$ iterations, each doing an $O(N)$ check.
Space Complexity: $O(N)$ auxiliary space to store the unrolled 1D points.
'''

import ast
from bisect import bisect_left
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        res = []
        
        # 1. Unroll the 2D perimeter into a 1D sorted array
        for x, y in points:
            if x == 0:
                res.append(y)
            elif y == side:
                res.append(side + x)
            elif x == side:
                res.append(side * 3 - y)
            else:
                res.append(side * 4 - x)
                
        res.sort()
        
        # 2. Validation function to check if a distance `n` is possible
        def check(n: int) -> bool:
            idx = [0] * k
            curr = res[0]
            
            # Fast first pass: assume the optimal configuration starts at res[0]
            for i in range(1, k):
                j = bisect_left(res, curr + n)
                if j == len(res):
                    return False
                idx[i] = j
                curr = res[j]
                
            # Check the circular wrap-around distance
            if curr - res[0] <= side * 4 - n:
                return True
            
            # 3. Sliding Pointer Shift: If res[0] failed, try starting at subsequent points
            # We only need to test starts up to idx[1], because after that we are just duplicating shifted configurations
            for start_idx in range(1, idx[1]):
                idx[0] = start_idx
                for j in range(1, k):
                    # Nudge the pointer forward until the gap is valid
                    while res[idx[j]] < res[idx[j - 1]] + n:
                        idx[j] += 1
                        if idx[j] == len(res):
                            return False
                            
                # Check the circular wrap-around distance again
                if res[idx[-1]] - res[idx[0]] <= side * 4 - n:
                    return True
                    
            return False
        
        # Binary Search on the value space
        # Max theoretical distance is the total perimeter divided evenly by k
        left = 1
        right = (side * 4) // k + 1
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid       # This distance works, save it
                left = mid + 1  # Try to find a larger minimum distance
            else:
                right = mid - 1 # This distance is too large
                
        return ans

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3464. Maximize Distance on Square Perimeter ---")
    try:
        side_input = input("Enter the side length (e.g., 2): ").strip()
        points_input = input("Enter points array (e.g., [[0,0],[0,2],[2,0],[2,2],[1,0]]): ").strip()
        k_input = input("Enter k (e.g., 3): ").strip()
        
        # Safely evaluate inputs
        parsed_side = int(side_input)
        parsed_points = ast.literal_eval(points_input)
        parsed_k = int(k_input)
            
        result = solution.maxDistance(parsed_side, parsed_points, parsed_k)
        print(f"\nOutput: Maximum Minimum Distance: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")