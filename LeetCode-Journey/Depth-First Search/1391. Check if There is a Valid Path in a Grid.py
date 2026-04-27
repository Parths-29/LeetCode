'''
Question: 1391. Check if There is a Valid Path in a Grid (Medium)
You are given an m x n grid. Each cell of the grid represents a street with a specific type of pipe (1 through 6) that dictates which directions it can connect to.
You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
Return true if there is a valid path, or false otherwise.

---
My Approach (Disjoint Set Union / Graph Connectivity):
1. Instead of running a complex BFS/DFS that has to track incoming and outgoing directions, we treat the grid as an undirected graph.
2. We flatten the 2D grid into a 1D index using `x * n + y` so we can use a standard Union-Find (DSU) data structure.
3. For every cell, we look at its pipe type (1-6) and attempt to connect it to its valid neighbors.
4. Crucially, we only `union` two cells if the current pipe points to the neighbor AND the neighbor's pipe is designed to receive it (e.g., if we point Left, the left neighbor must be pipe 1, 4, or 6).
5. After sweeping the entire grid and snapping all valid pieces together, we simply check if the start cell (0, 0) and the end cell (m-1, n-1) belong to the exact same connected component!

Time Complexity: O(M * N) where M and N are the grid dimensions. We sweep the grid once, and DSU operations take near O(1) time.
Space Complexity: O(M * N) auxiliary space for the DSU parent and size arrays.
'''

import ast
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Path Compression
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by Size
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        def get_id(x, y):
            return x * n + y

        # Connection Logic: Check if we point a certain way AND the neighbor accepts it
        def connect_left(x, y):
            if y - 1 >= 0 and grid[x][y - 1] in [1, 4, 6]:
                uf.union(get_id(x, y), get_id(x, y - 1))

        def connect_right(x, y):
            if y + 1 < n and grid[x][y + 1] in [1, 3, 5]:
                uf.union(get_id(x, y), get_id(x, y + 1))

        def connect_up(x, y):
            if x - 1 >= 0 and grid[x - 1][y] in [2, 3, 4]:
                uf.union(get_id(x, y), get_id(x - 1, y))

        def connect_down(x, y):
            if x + 1 < m and grid[x + 1][y] in [2, 5, 6]:
                uf.union(get_id(x, y), get_id(x + 1, y))

        # Sweep the grid and attempt connections based on pipe type
        for i in range(m):
            for j in range(n):
                pipe = grid[i][j]
                if pipe == 1:
                    connect_left(i, j)
                    connect_right(i, j)
                elif pipe == 2:
                    connect_up(i, j)
                    connect_down(i, j)
                elif pipe == 3:
                    connect_left(i, j)
                    connect_down(i, j)
                elif pipe == 4:
                    connect_right(i, j)
                    connect_down(i, j)
                elif pipe == 5:
                    connect_left(i, j)
                    connect_up(i, j)
                elif pipe == 6:
                    connect_right(i, j)
                    connect_up(i, j)

        # Are the start and end nodes in the same connected component?
        return uf.find(get_id(0, 0)) == uf.find(get_id(m - 1, n - 1))

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 1391. Check if There is a Valid Path in a Grid Interactive Runner ---")
    try:
        grid_input = input("Enter the 2D grid array (e.g., [[2,4,3],[6,5,2]]): ").strip()
        
        # Safely evaluate input
        parsed_grid = ast.literal_eval(grid_input)
        
        if not isinstance(parsed_grid, list) or not isinstance(parsed_grid[0], list):
            raise ValueError("Input must be a valid 2D list of integers.")
            
        result = solution.hasValidPath(parsed_grid)
        print(f"\nIs there a valid path? {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")