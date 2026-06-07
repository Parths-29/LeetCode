'''
Question: 2196. Create Binary Tree From Descriptions (Medium)
You are given a 2D integer array descriptions where descriptions[i] = [parent_i, child_i, isLeft_i] indicates that parent_i is the parent of child_i in a binary tree of unique values.
- If isLeft_i == 1, then child_i is the left child of parent_i.
- If isLeft_i == 0, then child_i is the right child of parent_i.
Construct the binary tree described by these descriptions and return its root.

---
My Approach (Hash Map + In-Degree Root Tracking):
1. We iterate through the descriptions stream in O(N) time.
2. We dynamically instantiate `TreeNode` objects and store them in a dictionary `nodes` mapped by their integer value. This allows O(1) retrieval and linking.
3. We link the `left` or `right` pointers strictly based on the `isLeft` flag.
4. Graph Theory Invariant: The root of a tree is the only node that is NEVER someone else's child. We add all `child` values to a `children` set.
5. Pythonic Optimization: We find the root by taking the set difference between all created node keys and the children set, extracting the single remaining value in C-optimized time.

Time Complexity: O(N) where N is the number of descriptions.
Space Complexity: O(N) auxiliary space to store the nodes and the children set.
'''

import ast
from typing import List, Optional
from collections import deque

# --- Definition for a binary tree node ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, is_left in descriptions:
            # Instantiate nodes if they don't exist yet
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
                
            # Link the nodes together
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
                
            # Track nodes that have incoming edges
            children.add(child)
            
        # The root is the only node that has NO incoming edges (In-Degree = 0)
        # Using Python set difference for an ultra-fast O(N) extraction
        root_val = (set(nodes.keys()) - children).pop()
        
        return nodes[root_val]

# --- Local Testing Helpers ---
def serialize_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Serializes a binary tree into a level-order array (LeetCode format)."""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
            
    # Clean up trailing Nones for a clean output
    while result and result[-1] is None:
        result.pop()
        
    return result

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 2196. Create Binary Tree From Descriptions ---")
    try:
        desc_input = input("Enter descriptions array (e.g., [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]): ").strip()
        
        # Safely evaluate input
        parsed_desc = ast.literal_eval(desc_input)
        
        if not isinstance(parsed_desc, list) or not isinstance(parsed_desc[0], list):
            raise ValueError("Input must be a valid 2D list of integers.")
            
        root_node = solution.createBinaryTree(parsed_desc)
        output_array = serialize_tree(root_node)
        
        print(f"\nConstructed Tree (Level-Order Array): {output_array}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")