'''
Question: 143. Reorder List (Medium)
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

---
My Approach (Find Mid + Reverse + Merge):
1. Find the Middle: Use a `slow` and `fast` pointer to find the middle of the linked list. By the time `fast` reaches the end, `slow` will be at the midpoint.
2. Reverse the Second Half: Sever the connection between the first half and the second half (`slow.next = None`). Then, standardly reverse the second half of the list starting from `second`.
3. Merge Alternately: Set two pointers, `first` at the head of the first half, and `second` at the head of the reversed second half. Zip them together by meticulously reassigning their `.next` pointers step-by-step.

Time Complexity: O(N) where N is the number of nodes in the list. We do a few passes, but it scales linearly.
Space Complexity: O(1) as we only rearrange existing node pointers without allocating any extra memory.
'''

import ast
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # 1. Find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Merge
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

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
    
    print("--- 143. Reorder List Interactive Runner ---")
    try:
        # Responsive input setup
        head_input = input("Enter the linked list as an array (e.g., [1,2,3,4]): ")
        parsed_head = ast.literal_eval(head_input)
        
        if not isinstance(parsed_head, list):
            raise ValueError("Input must be a list.")
            
        # Build the linked list
        linked_list_head = build_linked_list(parsed_head)
        
        # Call the function (modifies the list in-place)
        solution.reorderList(linked_list_head)
        
        # Convert back to list for easy printing
        result_array = linked_list_to_list(linked_list_head)
        print(f"\nOutput: {result_array}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")