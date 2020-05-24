class LongestSubsWOutRpt:

    @staticmethod
    def length_of_longest_substring(input_str):
        seen = {}
        max_sub_length = 0
        current_length = 0
        for i in range(len(input_str)):
            char = input_str[i]
            if char in seen:
                last_seen_index = seen[char]
                if last_seen_index >= i - current_length:
                    # in current subs
                    max_sub_length = max(max_sub_length, current_length)
                    current_length = i - last_seen_index - 1
            seen[char] = i
            current_length += 1
        max_sub_length = max(current_length, max_sub_length)
        return max_sub_length
