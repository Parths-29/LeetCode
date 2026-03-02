'''
Question: 141. Linked List Cycle (Easy)
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true

Example 3:
Input: head = [1], pos = -1
Output: false

---
My Approach (Floyd's Tortoise and Hare):
1. Initialize two pointers, `slow` and `fast`, both starting at the `head` of the linked list.
2. Traverse the list: `slow` moves 1 step at a time (`slow = slow.next`), and `fast` moves 2 steps at a time (`fast = fast.next.next`).
3. If the linked list has a cycle, the `fast` pointer will loop around and eventually point to the exact same node as the `slow` pointer. If `slow == fast`, return True.
4. If there is no cycle, the `fast` pointer will eventually reach the end of the list (`None`). If this happens, the loop breaks and we return False.

Time Complexity: O(N) where N is the number of nodes. In the worst case, we traverse the list a few times.
Space Complexity: O(1) because we only use two pointers, requiring no extra memory.
'''

import ast
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        # Keep going as long as fast hasn't reached the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there is a cycle
            if slow == fast:
                return True
                
        return False

# --- Interactive Driver Code ---
def build_linked_list_with_cycle(arr, pos):
    if not arr:
        return None
        
    head = ListNode(arr[0])
    curr = head
    nodes = [head] # Keep track of nodes by index
    
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
        
    # Create the cycle if pos is valid
    if pos != -1 and 0 <= pos < len(nodes):
        curr.next = nodes[pos]
        
    return head

if __name__ == "__main__":
    solution = Solution()
    
    print("--- 141. Linked List Cycle Interactive Runner ---")
    try:
        head_input = input("Enter the linked list as an array (e.g., [3,2,0,-4]): ")
        pos_input = input("Enter the pos integer (e.g., 1, or -1 for no cycle): ")
        
        parsed_head = ast.literal_eval(head_input)
        pos = int(pos_input)
        
        if not isinstance(parsed_head, list):
            raise ValueError("Head input must be a list.")
            
        # Build the linked list with the hidden cycle
        linked_list_head = build_linked_list_with_cycle(parsed_head, pos)
        
        # Calling the function
        result = solution.hasCycle(linked_list_head)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")