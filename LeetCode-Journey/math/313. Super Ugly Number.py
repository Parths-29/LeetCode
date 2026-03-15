'''
Question: 313. Super Ugly Number (Medium)
A super ugly number is a positive integer whose prime factors are in the array primes.
Given an integer n and an array of integers primes, return the nth super ugly number.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

---
My Approach (Min-Heap / Priority Queue):
1. We need to generate super ugly numbers in strictly increasing order.
2. Initialize an array `nums` of size `n` to store the sequence, starting with `nums[0] = 1`.
3. Create a Min-Heap. For each prime in our `primes` array, push a tuple: `(prime_value, prime, index)`. 
   - `prime_value` is the current generated multiple.
   - `prime` is the base prime factor.
   - `index` is the pointer to the `nums` array to multiply with next.
4. Loop until we've found `n` numbers. Pop the smallest `prime_value` from the heap.
5. To avoid duplicates (like 2*7 and 7*2 both creating 14), only add the `prime_value` to `nums` if it's strictly greater than the last added number.
6. Push the next multiple for that specific prime back into the heap: `(prime * nums[index + 1], prime, index + 1)`.
7. Return the last element in the `nums` array.

Time Complexity: $O(N \log K)$ where N is the target number and K is the length of the primes array. Each heap pop/push takes $O(\log K)$.
Space Complexity: $O(N + K)$ to store the sequence array of size N and the heap of size K.
'''

import ast
import heapq
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
            
        # Min-heap stores tuples: (current_val, base_prime, index_in_nums)
        heap = []
        for p in primes:
            heapq.heappush(heap, (p, p, 0))

        nums = [0] * n
        nums[0] = 1
        
        i = 1
        while i < n:
            current_val, prime, index = heapq.heappop(heap)
            
            # Remove duplicate logic
            if current_val != nums[i - 1]:
                nums[i] = current_val
                i += 1
                
            # Push the next multiple for this prime
            heapq.heappush(heap, (prime * nums[index + 1], prime, index + 1))
            
        return nums[n - 1]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 313. Super Ugly Number Interactive Runner ---")
    try:
        n_input = input("Enter the integer n (e.g., 12): ").strip()
        primes_input = input("Enter the primes array (e.g., [2,7,13,19]): ")
        
        n = int(n_input)
        parsed_primes = ast.literal_eval(primes_input)
        
        if not isinstance(parsed_primes, list):
            raise ValueError("Primes input must be a list.")
            
        # Calling the function
        result = solution.nthSuperUglyNumber(n, parsed_primes)
        print(f"\nOutput: {result}")
        
    except Exception as e:
        print(f"Error parsing input. Details: {e}")