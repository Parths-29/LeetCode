'''
Question: 98. Validate Binary Search Tree (Medium)
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

---
My Approach (Iterative In-Order Traversal):
1. The fundamental property of a valid BST is that an In-Order Traversal (Left -> Root -> Right) will ALWAYS produce a strictly increasing sequence of values.
2. Instead of using recursion (which is vulnerable to call stack limits on deep/skewed trees), we simulate the call stack manually using a list `stack`.
3. We traverse as far left as possible, pushing nodes onto the stack.
4. When we can't go left anymore, we pop the top node from the stack. This is the next smallest element in the tree.
5. Optimization: Instead of storing the whole traversal in an array to check if it's sorted, we only store the `prev` value. If our current popped node's value is ever less than or equal to `prev`, the strictly-increasing rule is broken, and we return False.
6. We then move to the right child and repeat.

Time Complexity: $O(N)$ where N is the number of nodes. We visit each node exactly once.
Space Complexity: $O(H)$ where H is the height of the tree. In the worst case (a perfectly skewed tree), this is $O(N)$. In a balanced tree, it is $O(\log N)$.
'''

import ast
from typing import Optional, List
from collections import deque

# --- Definition for a binary tree node ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        prev = None

        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process the node
            curr = stack.pop()

            # The current value must be strictly greater than the previous value
            if prev is not None and curr.val <= prev:
                return False

            # Update prev and move right
            prev = curr.val
            curr = curr.right

        return True

# --- Local Testing Helpers ---
def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order traversal list (LeetCode format)."""
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        
        # Left Child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        # Right Child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 98. Validate Binary Search Tree Interactive Runner ---")
    try:
        # Expected input format: [2,1,3] or [5,1,4,None,None,3,6]
        tree_input = input("Enter tree array in level-order (e.g., [2,1,3]): ").strip()
        
        # Safely evaluate input replacing 'null' with 'None' if user pastes directly from LeetCode
        tree_input = tree_input.replace('null', 'None')
        parsed_tree_list = ast.literal_eval(tree_input)
        
        if not isinstance(parsed_tree_list, list):
            raise ValueError("Input must be a valid list.")
            
        root_node = build_tree_from_list(parsed_tree_list)
        result = solution.isValidBST(root_node)
        
        print(f"\nIs Valid BST? {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")