def champagneTower(poured, query_row, query_glass):
    '''
    Approach:

    Use 2D DP simulation.

    1️⃣ Create a 2D array of size 101x101 (since max row = 100).
    2️⃣ Pour all champagne into dp[0][0].
    3️⃣ For each glass:
          If it has more than 1 cup,
          compute overflow = (amount - 1) / 2
          distribute to next row left and right.
    4️⃣ Return min(1, dp[query_row][query_glass])
       because a glass cannot hold more than 1.
    '''

    dp = [[0.0] * 101 for _ in range(101)]
    dp[0][0] = poured

    for r in range(100):
        for c in range(r + 1):
            if dp[r][c] > 1:
                overflow = (dp[r][c] - 1) / 2
                dp[r + 1][c] += overflow
                dp[r + 1][c + 1] += overflow
                dp[r][c] = 1  # cap it at 1

    return min(1, dp[query_row][query_glass])


# ====== INPUT / OUTPUT ======
poured = int(input("Enter poured amount: "))
query_row = int(input("Enter query row: "))
query_glass = int(input("Enter query glass: "))
print("Champagne in glass:", champagneTower(poured, query_row, query_glass))
