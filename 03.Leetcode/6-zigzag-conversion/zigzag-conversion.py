class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of empty strings to store characters for each row
        rows = [''] * numRows
        
        # Direction flag to track the direction of movement in the zigzag pattern
        direction = 1
        # Current row index
        row_index = 0
        
        for char in s:
            rows[row_index] += char  # Add current character to the appropriate row
            # Change direction if at the top or bottom row
            if row_index == 0:
                direction = 1
            elif row_index == numRows - 1:
                direction = -1
            row_index += direction  # Move to the next row
        
        # Concatenate all rows to get the result
        return ''.join(rows)

# Example usage:
s = Solution()
print(s.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(s.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(s.convert("A", 1))               # Output: "A"
