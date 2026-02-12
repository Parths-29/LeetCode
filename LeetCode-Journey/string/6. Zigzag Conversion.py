'''
The Zigzag Bounce
Intuition - 
Think of this problem like filling buckets. You have a set number of rows (buckets). You hold a ball (character) and drop it into the first bucket, then the second, until you hit the bottom. Then, you bounce back up to the top. We just need to follow this bouncing path and collect the characters row by row at the end.
Approach -
We create a list of empty strings, one for each row. We iterate through the input string and place each character into its current row. The trick is a simple "step" variable: it starts as $+1$ (moving down). When we hit the bottom row, we flip it to $-1$ (moving up). When we hit the top again, we flip it back.
'''
def convert(s, numRows):
    # Edge case: no zigzag needed
    if numRows == 1 or numRows >= len(s):
        return s

    # Create a list for each row
    rows = [""] * numRows

    curr_row = 0
    going_down = False  # direction flag

    for char in s:
        # Add character to current row
        rows[curr_row] += char

        # Reverse direction if we hit top or bottom
        if curr_row == 0 or curr_row == numRows - 1:
            going_down = not going_down

        # Move row pointer
        if going_down:
            curr_row += 1
        else:
            curr_row -= 1

    # Join all rows
    return "".join(rows)


# ====== INPUT / OUTPUT ======
s = input("Enter string: ")
numRows = int(input("Enter number of rows: "))
print("Zigzag conversion:", convert(s, numRows))
