'''
Question: 1914. Cyclically Rotating a Grid (Medium)
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.
The matrix is composed of several layers. You need to cyclically rotate the matrix counter-clockwise by k steps.

---
My Approach (1D Array Unrolling):
1. Simulating the rotation step-by-step takes O(K * Perimeter) time, which is slow for large K.
2. Instead, we extract each 2D ring (layer) into a 1D array.
3. We calculate the effective shifts using modulo: `shifts = k % len(1d_array)`.
4. Because rotating a ring counter-clockwise exactly maps to shifting a 1D array to the left, we can just start reading from the `shifts` index of our 1D array (wrapping around using modulo).
5. We walk the perimeter one last time, writing the shifted values back into the grid.

Time Complexity: O(M * N) where M and N are grid dimensions. Every cell is extracted once and written once.
Space Complexity: O(M + N) auxiliary space to store the perimeter of the largest layer.
'''

from typing import List
import ast

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        top, bottom = 0, len(grid) - 1
        left, right = 0, len(grid[0]) - 1

        while top < bottom and left < right:
            # 1. Unroll the layer into a 1D array
            layer = []
            
            # Top row (Left to Right)
            for j in range(left, right + 1):
                layer.append(grid[top][j])
            # Right column (Top+1 to Bottom)
            for i in range(top + 1, bottom + 1):
                layer.append(grid[i][right])
            # Bottom row (Right-1 to Left)
            for j in range(right - 1, left - 1, -1):
                layer.append(grid[bottom][j])
            # Left column (Bottom-1 to Top+1)
            for i in range(bottom - 1, top, -1):
                layer.append(grid[i][left])

            # 2. Calculate the effective rotation
            perimeter = len(layer)
            shifts = k % perimeter

            # 3. Write back into the grid using the exact same traversal pattern
            # We start reading from our `shifts` offset
            idx = shifts 
            
            # Top row
            for j in range(left, right + 1):
                grid[top][j] = layer[idx % perimeter]
                idx += 1
            # Right column
            for i in range(top + 1, bottom + 1):
                grid[i][right] = layer[idx % perimeter]
                idx += 1
            # Bottom row
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = layer[idx % perimeter]
                idx += 1
            # Left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = layer[idx % perimeter]
                idx += 1

            # Move to the inner layer
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return grid

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 1914. Cyclically Rotating a Grid ---")
    try:
        grid_input = input("Enter the 2D grid array (e.g., [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]): ").strip()
        k_input = input("Enter k (e.g., 2): ").strip()
        
        parsed_grid = ast.literal_eval(grid_input)
        parsed_k = int(k_input)
            
        result = solution.rotateGrid(parsed_grid, parsed_k)
        print("\nRotated Grid:")
        for row in result:
            print(row)
        '''
        except ValueError:'''
    except Exception as e:
        print(f"An unexpected error occurred: {e}")