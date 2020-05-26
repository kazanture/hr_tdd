"""
https://leetcode.com/problems/string-to-integer-atoi/
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

"""
class StringToInteger:
    def my_atoi(self, str_num: str) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        val = ""
        n_m = 1
        for char in str_num:
            if (char == '-' or char == '+') and val == "":
                val = char
                continue
            elif '0' <= char <= '9':
                val += char
            elif char == ' ' and val == "":
                continue
            else:
                break
        if val == '' or val == '-' or val == '+':
            val = 0
        val = int(val)
        if val > MAX_INT:
            return MAX_INT
        if val < MIN_INT:
            return MIN_INT
        return val