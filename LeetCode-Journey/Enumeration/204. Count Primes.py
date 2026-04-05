'''
Question: 204. Count Primes (Medium)
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

---
My Approach (Lucy's Algorithm / Meissel-Lehmer DP):
1. The standard Sieve of Eratosthenes requires O(N) space, which can hit Memory Limit Exceeded (MLE) in Python for massive values of N.
2. We optimize space to O(sqrt(N)) by only sieving primes up to the square root of N.
3. We use a recursive Dynamic Programming function `g(v, p)` to calculate the number of integers up to `v` that are coprime to the first `p` primes.
4. The transition is: g(v, p) = g(v, p-1) - (g(v // prime, p-1) - g(prime-1, p-1)).
   - This effectively removes all multiples of the current prime, adjusting for numbers that were already removed by smaller primes.
5. If prime * prime > v, we can stop early, drastically cutting down the time complexity.

Time Complexity: Sub-linear, approximately O(N^(3/4)) or O(N^(2/3)) depending on implementation overhead. Vastly outperforms standard O(N log log N) Sieve at massive scales.
Space Complexity: O(sqrt(N)) to store the primes up to the square root of N.
'''

class Solution:
    def __init__(self) -> None:
        self.primes: list[int] = []
        self.n: int = 0
        self.n_sqrt: int = 0
    
    def sieve(self) -> None:
        n: int = self.n_sqrt
        is_prime: list[bool] = [True] * (n + 2)
        for i in range(2, n + 1):
            if is_prime[i]:
                self.primes.append(i)
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

    def isqrt(self, n: int) -> int:
        if n <= 1:
            return n
        r2: int = 2 * self.isqrt(n >> 2)
        r3: int = r2 + 1
        return r2 if (n < r3 * r3) else r3
    
    def find_prime_number(self, n: int) -> int:
        l, r = 0, len(self.primes) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if self.primes[m] <= n:
                l = m
            else:
                r = m - 1
        if self.primes[l] > n:
            l -= 1
        return l
    
    def g(self, n: int, prime_index: int) -> int:
        if prime_index == -1:
            return n - 1
            
        prime: int = self.primes[prime_index]
        s: int = self.g(n, prime_index - 1)
        
        if prime * prime <= n:
            s -= (self.g(n // prime, prime_index - 1) - self.g(prime - 1, prime_index - 1))
        return s
    
    def lucy(self, n: int) -> int:
        prime_index: int = self.find_prime_number(self.n_sqrt)
        return self.g(n, prime_index)

    def countPrimes(self, n: int) -> int:
        # Corner cases where no primes < isqrt(n):
        if n <= 2:
            return 0
        if n <= 4:
            return n // 2

        # lucy calculates sum up to n; decrease by 1 to not count itself if n is prime
        self.n = n - 1
        self.n_sqrt = self.isqrt(self.n)
        self.sieve()
        return self.lucy(self.n)

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    
    print("--- 204. Count Primes (Lucy's Algorithm) Interactive Runner ---")
    try:
        n_input = input("Enter the integer n (e.g., 5000000): ").strip()
        
        # Safely evaluate input
        n = int(n_input)
            
        # Calling the function
        result = solution.countPrimes(n)
        print(f"\nOutput: {result}")
        
    except ValueError:
        print("Error: Input must be a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")