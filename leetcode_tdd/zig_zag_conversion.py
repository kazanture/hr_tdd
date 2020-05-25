"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""
class ZigZagConversion:
    def convert(self, input_str, num_rows):
        row = 0
        inc = 1
        res = [""] * num_rows
        for i in range(len(input_str)):
            if row == num_rows - 1:
                inc = -1
            if row == 0:
                inc = 1
            res[row] += input_str[i]
            if num_rows > 1:
                row += inc
        res_str = ""
        for row in res:
            res_str += row
        return res_str
