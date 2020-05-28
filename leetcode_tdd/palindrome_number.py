"""
https://leetcode.com/problems/palindrome-number/
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""


class PalindromeNumber:
    def get_number_of_digits(self, number):
        if number == 0:
            return 1
        if number < 0:
            number = -1 * number
        digits = 0
        while number > 0:
            number = number // 10
            digits += 1
        return digits

    def is_palindrome(self, number):
        if number < 0:
            return False
        stack = []
        digits = self.get_number_of_digits(number)
        num = number
        for i in range(digits // 2):
            stack.append(num % 10)
            num = num // 10
        if digits > 1 and digits % 2 == 1:
            # skip middle digit
            num = num // 10
        for i in range(digits // 2):
            val1 = stack.pop()
            val2 = num % 10
            if val1 != val2:
                return False
            num = num // 10
        return True
