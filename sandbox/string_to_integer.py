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