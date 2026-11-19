import sys

input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        zeros = s.count('0')
        ones = n - zeros
        
        # Maximize the majority character using at most k flips
        big = max(zeros, ones)
        small = min(zeros, ones)
        
        moved = min(small, k)
        big += moved
        small -= moved
        
        ans = 1 + (big * (big + 1) // 2) + (small * (small + 1) // 2)
        results.append(str(ans))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()