"""
Problem: 1022. Sum of Root To Leaf Binary Numbers
Difficulty: Easy

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
The test cases are generated so that the answer fits in a 32-bits integer.

My Approach:
- Used Depth-First Search (DFS) to traverse down to the leaves.
- Shifted the binary value left (2 * n) and added the current node's value at each step.
- Added the final computed binary value to a global answer variable when a leaf is hit.
"""

import ast
from collections import deque
from typing import Optional

# 1. Boilerplate: LeetCode's TreeNode Class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2. Boilerplate: Helper to convert an array into a Binary Tree
def build_tree(values: list) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root

# 3. Your Core Logic
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, n = 0) -> None:
            if not node: return

            n = 2 * n + node.val
            if not node.left and not node.right:
                self.ans += n
                return
                
            dfs(node.left , n)
            dfs(node.right, n)
            return
            
        self.ans = 0
        dfs(root)
        return self.ans

# 4. The Execution Block for VS Code Terminal
if __name__ == "__main__":
    print("--- 1022. Sum of Root To Leaf Binary Numbers ---")
    
    user_input = input("Enter the tree array (e.g., [1,0,1,0,1,0,1]): ")
    
    try:
        formatted_input = user_input.replace('null', 'None')
        values = ast.literal_eval(formatted_input)
        
        root = build_tree(values)
        
        solution = Solution()
        result = solution.sumRootToLeaf(root)
        
        print(f"\nOutput: {result}\n")
        
    except Exception as e:
        print(f"\nError: Please make sure you enter a valid array format. Details: {e}")