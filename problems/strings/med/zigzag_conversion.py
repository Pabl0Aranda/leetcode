"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 
Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

def ZigZag_Conversion(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # Create a list to hold each row's characters
    rows = ['' for _ in range(numRows)]
    current_row = 0
    going_down = False

    # Iterate through each character in the input string
    for char in s:
        rows[current_row] += char
        # Reverse direction when we hit the top or bottom row
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # Move up or down depending on the direction
        current_row += 1 if going_down else -1

    # Join all rows to get the final zigzag string
    return ''.join(rows)

# Test cases
def test_convert_ZigZag():
    assert ZigZag_Conversion("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", "Failed test case 1"
    assert ZigZag_Conversion("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", "Failed test case 2"
    assert ZigZag_Conversion("A", 1) == "A", "Failed test case 3"
    assert ZigZag_Conversion("AB", 1) == "AB", "Failed test case 4"
    assert ZigZag_Conversion("ABC", 2) == "ACB", "Failed test case 5"
    print("All test cases passed.")

test_convert_ZigZag()