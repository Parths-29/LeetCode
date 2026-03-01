'''
Question: 61. Rotate List (Medium)
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

---
My Approach (Circular Linked List):
1. Handle edge cases: If the list is empty, has only one node, or `k == 0`, just return the head.
2. Find the length of the linked list and locate the final `tail` node.
3. Connect the `tail.next` to the `head`. This turns the list into a continuous circle.
4. Optimize `k`: If `k` is larger than the length of the list, rotating it is repetitive. We only need the effective rotations: `k = k % length`.
5. Find the *new* tail. If we shift right by `k`, the new tail will be at position `length - k` from the start.
6. Traverse to the new tail. The node right after it is our `new_head`.
7. Break the circle by setting `new_tail.next = None`.
8. Return the `new_head`.

Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1) as we only use a few pointers.
'''

import ast
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1 & 2: Find the length and the current tail
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 3: Connect tail to head to form a circle
        tail.next = head
        
        # Step 4 & 5: Find the step count to the new tail
        k = k % length
        steps_to_new_tail = length - k
        
        # Step 6: Traverse to the new tail
        new_tail = tail
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # Step 7 & 8: Break the circle and return the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head

# --- Interactive Driver Code ---
def build_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    solution = Solution()
    
    print("--- 61. Rotate List Interactive Runner ---")
    try:
        head_input = input("Enter the linked list as an array (e.g., [1,2,3,4,5]): ")
        k_input = input("Enter the integer k (e.g., 2): ")
        
        # Safely evaluate inputs
        parsed_head = ast.literal_eval(head_input)
        k = int(k_input)
        
        if not isinstance(parsed_head, list):
            raise ValueError("Head input must be a list.")
            
        # Convert Python list to Linked List
        linked_list_head = build_linked_list(parsed_head)
        
        # Calling the function
        result_node = solution.rotateRight(linked_list_head, k)
        
        # Convert the resulting Linked List back to a Python list for printing
        result_array = linked_list_to_list(result_node)
        print(f"\nOutput: {result_array}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")