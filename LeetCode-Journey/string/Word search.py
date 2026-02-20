def exist(board, word):
    '''
    Approach:

    1️⃣ Try every cell as starting point.
    2️⃣ Use DFS to explore 4 directions.
    3️⃣ Mark cell as visited temporarily.
    4️⃣ Backtrack after exploring.
    '''

    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        # If entire word matched
        if index == len(word):
            return True

        # Check boundaries and character match
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            board[r][c] != word[index]):
            return False

        # Mark as visited
        temp = board[r][c]
        board[r][c] = "#"

        # Explore 4 directions
        found = (
            dfs(r + 1, c, index + 1) or
            dfs(r - 1, c, index + 1) or
            dfs(r, c + 1, index + 1) or
            dfs(r, c - 1, index + 1)
        )

        # Restore cell (backtrack)
        board[r][c] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


# ====== INPUT / OUTPUT ======
rows = int(input("Enter number of rows: "))
board = []

for _ in range(rows):
    board.append(input("Enter row characters without space: ").strip().split())

word = input("Enter word to search: ")

print("Word exists:", exist(board, word))