'''
Question: 860. Lemonade Change (Easy)
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Return true if and only if you can provide every customer with the correct change.

Example 1:
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:
Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

---
My Approach (Greedy Algorithm):
1. We only need to track the count of $5 and $10 bills. ($20 bills are useless for making change).
2. If a customer gives $5, we just increment our $5 count.
3. If a customer gives $10, we must give a $5 in change. If we don't have one, return False. Otherwise, decrement $5 and increment $10.
4. If a customer gives $20, we use a greedy approach:
   - Try to give one $10 and one $5 first, because $5 bills are more valuable/versatile for future transactions.
   - If we don't have a $10, fall back to giving three $5 bills.
   - If neither option is possible, we can't make change, so return False.
5. If we make it through the entire line, return True.

Time Complexity: $O(N)$ where N is the length of the bills array. We process each customer exactly once.
Space Complexity: $O(1)$ auxiliary space as we only use two integer variables for tracking.
'''

import ast
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                # Greedy choice: prefer getting rid of a $10 and a $5
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                # Fallback: use three $5s
                elif five >= 3:
                    five -= 3
                else:
                    return False
                    
        return True

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 860. Lemonade Change Interactive Runner ---")
    try:
        bills_input = input("Enter the queue of bills (e.g., [5,5,5,10,20]): ").strip()
        
        # Safely evaluate input
        parsed_bills = ast.literal_eval(bills_input)
        
        if not isinstance(parsed_bills, list):
            raise ValueError("Input must be a list of integers.")
            
        # Calling the function
        result = solution.lemonadeChange(parsed_bills)
        print(f"\nOutput: {result}")
        
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")