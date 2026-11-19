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
        ans = n * (n + 1) // 2
        min_flips = min(s.count('0'), s.count('1'))
        if min_flips <= k:
            ans += 1
        results.append(str(ans))  # Fixed: 'results' (plural), not 'result'
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()