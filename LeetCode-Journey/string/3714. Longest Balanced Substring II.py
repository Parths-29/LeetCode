'''
Keep running counts of a, b, c.

Compute (countA - countB, countA - countC).

Store first occurrence of each pair in hashmap.

If same pair appears again → update max length.

Return max length.'''
def longestBalancedSubstring(s):
    countA = countB = countC = 0
    
    # Map to store first occurrence of (diffAB, diffAC)
    seen = {(0, 0): -1}
    
    max_len = 0
    
    for i in range(len(s)):
        # Update counts
        if s[i] == 'a':
            countA += 1
        elif s[i] == 'b':
            countB += 1
        else:  # 'c'
            countC += 1
        
        # Calculate differences
        diffAB = countA - countB
        diffAC = countA - countC
        
        key = (diffAB, diffAC)
        
        # If we've seen this state before, substring is balanced
        if key in seen:
            max_len = max(max_len, i - seen[key])
        else:
            # Store first time we see this difference
            seen[key] = i
    
    return max_len


# ====== INPUT / OUTPUT ======
s = input("Enter string (a,b,c only): ")
print("Longest balanced substring length:", longestBalancedSubstring(s))
