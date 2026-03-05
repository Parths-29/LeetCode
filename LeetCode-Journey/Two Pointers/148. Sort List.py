'''
Question: 148. Sort List (Medium)
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

---
My Approach (Extract, Sort, and Replace):
1. Check for edge cases: if the list is empty or has only one node, it's already sorted.
2. Traverse the linked list and append every node's value into a Python list `a`.
3. Sort the list `a` using Python's built-in `.sort()` method.
4. Traverse the linked list a second time from the `head`.
5. Overwrite each node's `.val` with the corresponding sorted value from `a`.
6. Return the original `head` (which now contains the sorted values).

Time Complexity: $O(N \\log N)$ because Python's `.sort()` takes $O(N \\log N)$ time, and the two traversals take $O(N)$ time.
Space Complexity: $O(N)$ because we store all the values in an auxiliary array `a`.
'''

import ast
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # checking if empty or single length
        if not head or not head.next: 
            return head 
            
        c = head 
        a = [] 
        
        # till we reach the end of a list 
        while c: 
            a.append(c.val) 
            c = c.next 
            
        # sorting our array
        a.sort() 
        
        # now we gonna store sorted values one by one
        c = head 
        i = 0
        
        # traverse again to overwrite values
        while c: 
            c.val = a[i] 
            c = c.next 
            i += 1 
            
        # returning the sorted list
        return head 

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
    
    print("--- 148. Sort List Interactive Runner ---")
    try:
        head_input = input("Enter the linked list as an array (e.g., [4,2,1,3]): ")
        parsed_head = ast.literal_eval(head_input)
        
        if not isinstance(parsed_head, list):
            raise ValueError("Input must be a list.")
            
        # Build the linked list
        linked_list_head = build_linked_list(parsed_head)
        
        # Call the function
        result_head = solution.sortList(linked_list_head)
        
        # Convert back to list for easy printing
        result_array = linked_list_to_list(result_head)
        print(f"\nOutput: {result_array}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")