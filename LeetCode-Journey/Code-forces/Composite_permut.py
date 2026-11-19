import sys
input = sys.stdin.read
def solve():
    data = input().split()
    if not data:
        return
    t = int(data[0])
    results=[]
    for idx in range(1,t+1):
        n = int(data[idx])
        if n < 4:
            results.append("-1")
        else:
            p = list(range(1,n+1))
            p[0], p[3] = p[3] , p[0]
            results.append(" ".join(map(str,p)))
    sys.stdout.write("\n".join(results)+"\n")
if __name__ == "__main__":
    solve()