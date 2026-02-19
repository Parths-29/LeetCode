def minDistance(word1, word2):
    '''
    Approach:

    dp[i][j] = minimum operations to convert
               first i characters of word1
               into first j characters of word2.

    If characters match:
        dp[i][j] = dp[i-1][j-1]

    Else:
        dp[i][j] = 1 + min(
            dp[i][j-1],    # insert
            dp[i-1][j],    # delete
            dp[i-1][j-1]   # replace
        )
    '''

    n, m = len(word1), len(word2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],    # insert
                    dp[i - 1][j],    # delete
                    dp[i - 1][j - 1] # replace
                )

    return dp[n][m]


# ====== INPUT / OUTPUT ======
word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
print("Minimum edit distance:", minDistance(word1, word2))
