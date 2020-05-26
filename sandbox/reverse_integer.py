"""
https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.

"""


class ReverseInteger:

    def reverse(self, num: int) -> int:
        res = 0
        # 32 bit means 10 digits max
        current_dp = 10000000000
        negative = -1 if num < 0 else 1
        num *= negative
        while num > 0:
            res += current_dp * (num % 10)
            num = num // 10
            current_dp = current_dp // 10
        res = res // (current_dp * 10)
        # if it is greater than 2^31(or negative); return 0
        if res > 2147483648:
            res = 0
        return res * negative
