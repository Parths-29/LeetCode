def isMatch(s, p):
    '''
    We use Dynamic Programming.

    dp[i][j] means:
    First i characters of string s
    match first j characters of pattern p.

    Transition rules:

    1️⃣ If characters match OR pattern has '.'
        dp[i][j] = dp[i-1][j-1]

    2️⃣ If pattern has '*'
        Two possibilities:
        - Treat '*' as zero occurrence:
              dp[i][j] = dp[i][j-2]
        - If preceding char matches:
              dp[i][j] |= dp[i-1][j]

    Final answer will be dp[len(s)][len(p)]
    '''

    n, m = len(s), len(p)

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True  # empty string matches empty pattern

    # Handle patterns like a*, a*b*, etc. matching empty string
    for j in range(2, m + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            # Case 1: direct match or '.'
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]

            # Case 2: '*'
            elif p[j - 1] == '*':
                # zero occurrence
                dp[i][j] = dp[i][j - 2]

                # one or more occurrence
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] |= dp[i - 1][j]

    return dp[n][m]


# ====== INPUT / OUTPUT ======
s = input("Enter string s: ")
p = input("Enter pattern p: ")
print("Matches:", isMatch(s, p))
