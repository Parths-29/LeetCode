'''
Question: 1559. Detect Cycles in 2D Grid (Medium/Hard)
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.
A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

---
My Approach (Disjoint Set Union / Union-Find):
1. Instead of a deep DFS that tracks parent nodes to avoid trivial back-edges, we treat the grid as an undirected graph and use DSU to detect cycles.
2. We flatten the 2D grid coordinates into a 1D index using `i * n + j`.
3. We sweep through the grid. For every cell, we check its UP (`i - 1`) and LEFT (`j - 1`) neighbors.
4. If a neighbor matches the current cell's character, we attempt to `unite` them in our DSU.
5. If the DSU tells us that these two cells ALREADY share the same root/parent, it means an alternative path already connects them. Connecting them directly now forms a cycle! We immediately return True.
6. The DSU is heavily optimized using Path Compression and Union by Size, guaranteeing near O(1) operations.

Time Complexity: O(M * N) where M and N are the dimensions of the grid. We visit each cell once, and DSU operations take near constant time.
Space Complexity: O(M * N) auxiliary space for the parent and size arrays in the DSU class.
'''

import ast
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.setCount = n
        self.parent = list(range(n))
        self.size = [1] * n

    def findset(self, x: int) -> int:
        # Path Compression: Flatten the tree to point directly to the root
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int):
        # Union by Size: Attach the smaller tree under the larger tree
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1

    def findAndUnite(self, x: int, y: int) -> bool:
        parentX, parentY = self.findset(x), self.findset(y)
        if parentX != parentY:
            self.unite(parentX, parentY)
            return True # Successfully united
        return False # Cycle detected! They are already connected.

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        
        for i in range(m):
            for j in range(n):
                # Check Up
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.findAndUnite(i * n + j, (i - 1) * n + j):
                        return True
                        
                # Check Left
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.findAndUnite(i * n + j, i * n + j - 1):
                        return True
                        
        return False

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 1559. Detect Cycles in 2D Grid Interactive Runner ---")
    try:
        # Example grid: [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
        grid_input = input("Enter the 2D grid array: ").strip()
        
        # Safely evaluate input
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or not isinstance(parsed_grid[0], list):
            raise ValueError("Input must be a valid 2D list of strings.")
            
        result = solution.containsCycle(parsed_grid)
        print(f"\nDoes the grid contain a cycle? {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")