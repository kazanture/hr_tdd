class LongestPalindromicSubs:

    def __init__(self):
        self.palindrome_storage = {}

    def is_palindrome(self, input_str):
        if input_str in self.palindrome_storage:
            return self.palindrome_storage[input_str]
        ret = False
        if len(input_str) < 2:
            ret = True
        elif len(input_str) == 2 and input_str[0] == input_str[1]:
            ret = True
        elif input_str[0] == input_str[-1]:
            ret = self.is_palindrome(input_str[1:-1])
        self.palindrome_storage[input_str] = ret
        return ret

    def longest_palindrome(self, input_str):
        pal = ""
        max_pal_length = 0
        for i in range(len(input_str)):
            if len(input_str) - i < max_pal_length:
                break
            for j in range(i+1, len(input_str) + 1):
                if j - i < max_pal_length:
                    continue
                print(i)
                print(max_pal_length)
                if self.is_palindrome(input_str[i:j]):
                    if j - i > max_pal_length:
                        max_pal_length = j - i
                        pal = input_str[i:j]
        return pal
