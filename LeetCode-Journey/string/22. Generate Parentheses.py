def generateParenthesis(n):
    '''
    Approach:

    Use backtracking with constraints.

    1️⃣ We can add '(' if open_count < n.
    2️⃣ We can add ')' if close_count < open_count.
    3️⃣ When string length == 2*n, add to result.

    This ensures we only build valid combinations.
    '''

    result = []

    def backtrack(current, open_count, close_count):
        # If full length reached
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add '(' if allowed
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        # Add ')' only if it won't break balance
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# ====== INPUT / OUTPUT ======
n = int(input("Enter n: "))
print("Parentheses combinations:", generateParenthesis(n))
