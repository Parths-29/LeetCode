'''
Question: 142. Linked List Cycle II (Medium)
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

---
My Approach (Floyd's Tortoise and Hare - Phase 1 & 2):
1. Phase 1 (Detect Cycle): Initialize `slow` and `fast` pointers at the head. Move `slow` by 1 step and `fast` by 2 steps. If they meet, a cycle exists. If `fast` reaches the end (None), there is no cycle, so return None.
2. Phase 2 (Find Entry Node): Once they meet, reset the `slow` pointer back to the `head` of the linked list.
3. Keep the `fast` pointer at the meeting point.
4. Move BOTH pointers forward exactly 1 step at a time.
5. Because of the math behind the loop sizes, the exact node where they meet again is the beginning of the cycle!
6. Return either pointer.

Time Complexity: O(N) where N is the number of nodes.
Space Complexity: O(1) as we only use two pointers.
'''

import ast
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        has_cycle = False
        
        # Phase 1: Detect Cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
                
        if not has_cycle:
            return None
            
        # Phase 2: Find the Entry
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow

# --- Interactive Driver Code ---
def build_linked_list_with_cycle(arr, pos):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    nodes = [head] 
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
    if pos != -1 and 0 <= pos < len(nodes):
        curr.next = nodes[pos]
    return head

def get_node_index(head, target_node):
    if not target_node: return -1
    idx = 0
    curr = head
    visited = set()
    while curr and curr not in visited:
        if curr == target_node: return idx
        visited.add(curr)
        curr = curr.next
        idx += 1
    return -1

if __name__ == "__main__":
    solution = Solution()
    print("--- 142. Linked List Cycle II Interactive Runner ---")
    try:
        head_input = input("Enter the linked list as an array (e.g., [3,2,0,-4]): ")
        pos_input = input("Enter the pos integer (e.g., 1, or -1 for no cycle): ")
        
        parsed_head = ast.literal_eval(head_input)
        pos = int(pos_input)
        
        if not isinstance(parsed_head, list):
            raise ValueError("Head input must be a list.")
            
        linked_list_head = build_linked_list_with_cycle(parsed_head, pos)
        result_node = solution.detectCycle(linked_list_head)
        
        if result_node:
            idx = get_node_index(linked_list_head, result_node)
            print(f"\nOutput: tail connects to node index {idx} (value: {result_node.val})")
        else:
            print("\nOutput: no cycle (null)")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")