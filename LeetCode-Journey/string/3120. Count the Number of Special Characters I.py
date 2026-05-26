'''
Question: 3120. Count the Number of Special Characters I (Easy)
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.

---
My Approach (Bitwise Masking + ASCII Modulo Arithmetic):
1. Instead of using Python Hash Sets which carry overhead, we use two 32-bit integers to act as highly efficient boolean arrays.
2. `masks[0]` tracks uppercase letters seen, `masks[1]` tracks lowercase letters seen.
3. We loop through the word and get the ASCII value of each character.
4. The condition `val >= 97` resolves to 1 for lowercase and 0 for uppercase, acting as our array index.
5. The core trick: `val & 31` (modulo 32) perfectly maps both 'A' and 'a' to 1, 'B' and 'b' to 2, etc. 
6. We shift a 1 by that mapped value and bitwise OR (`|=`) it into the respective mask.
7. Finally, `masks[0] & masks[1]` isolates the letters that appeared in both cases, and `.bit_count()` tallies them up.

Time Complexity: O(N) where N is the length of the string.
Space Complexity: O(1) auxiliary space (just an array of two integers).
'''

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        masks = [0, 0]
        
        for c in word:
            val = ord(c)
            # val >= 97 maps uppercase to index 0, lowercase to index 1
            # val & 31 maps 'a'/'A' to 1, 'z'/'Z' to 26
            masks[val >= 97] |= (1 << (val & 31))
            
        # Bitwise AND isolates characters seen in both masks
        return (masks[0] & masks[1]).bit_count()

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 3120. Count Special Characters I (Bitwise) ---")
    try:
        word_input = input("Enter the word string (e.g., aaAbcBC): ").strip()
        
        # Clean quotes if accidentally pasted
        if word_input.startswith(('"', "'")): 
            word_input = word_input[1:-1]
            
        result = solution.numberOfSpecialChars(word_input)
        print(f"\nNumber of Special Characters: {result}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")