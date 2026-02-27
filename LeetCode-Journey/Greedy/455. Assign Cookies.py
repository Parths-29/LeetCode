'''
Question: 455. Assign Cookies (Easy)
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

---
My Approach (Greedy + Two Pointers):
1. Sort both the children's greed array `g` and the cookie sizes array `s` in ascending order.
2. Initialize two pointers: `child` at 0 and `cookie` at 0.
3. Loop until either pointer reaches the end of its respective array.
4. If the current cookie is large enough to satisfy the current child (`s[cookie] >= g[child]`), it's a successful match! We move to the next child by incrementing the `child` pointer.
5. Regardless of whether the cookie was used or was too small, we must move to the next cookie by incrementing the `cookie` pointer.
6. Once the loop finishes, the value of the `child` pointer tells us exactly how many children were satisfied.

Time Complexity: O(N log N + M log M) where N and M are the lengths of the arrays, due to the sorting step.
Space Complexity: O(1) auxiliary space.
'''

import ast
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child = 0
        cookie = 0
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # The cookie is big enough, move to the next child
                child += 1
            
            # Always move to the next cookie
            cookie += 1
            
        return child

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 455. Assign Cookies Interactive Runner ---")
    try:
        g_input = input("Enter the greed array g (e.g., [1,2,3]): ")
        s_input = input("Enter the cookie sizes array s (e.g., [1,1]): ")
        
        # Safely evaluate the inputs into Python lists
        g = ast.literal_eval(g_input) 
        s = ast.literal_eval(s_input) 
        
        if not isinstance(g, list) or not isinstance(s, list):
            raise ValueError("Both inputs must be lists.")
            
        # Calling the function
        result = solution.findContentChildren(g, s)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")