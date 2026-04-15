'''
Question: 832. Flipping an Image (Easy)
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

---
My Approach (Pythonic List Comprehension + Bitwise XOR):
1. To flip a row horizontally, we can use Python's highly optimized slice reversing: `row[::-1]`.
2. To invert the bits (0 to 1, and 1 to 0), we use the bitwise XOR operator `^ 1`.
3. We can combine both of these operations into a single, highly readable nested list comprehension.

Time Complexity: O(N * M) where N is rows and M is columns. We visit every bit exactly once.
Space Complexity: O(1) auxiliary space (or O(N*M) to build the new output matrix).
'''

import ast
from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # row[::-1] reverses the row
        # bit ^ 1 inverts the 0 or 1
        return [[bit ^ 1 for bit in row[::-1]] for row in image]

# --- Interactive Driver Code ---
if __name__ == "__main__":
    solution = Solution()
    print("--- 832. Flipping an Image Interactive Runner ---")
    try:
        image_input = input("Enter the binary matrix (e.g., [[1,1,0],[1,0,1],[0,0,0]]): ").strip()
        
        # Safely evaluate inputs
        parsed_image = ast.literal_eval(image_input)
        
        if not isinstance(parsed_image, list) or (parsed_image and not isinstance(parsed_image[0], list)):
            raise ValueError("Input must be a 2D list of integers.")
            
        result = solution.flipAndInvertImage(parsed_image)
        print(f"\nOutput: {result}")
    except ValueError as ve:
        print(f"Error parsing input. Details: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")