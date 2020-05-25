import pytest

from leetcode_tdd.longest_palindromic_subs import LongestPalindromicSubs

class TestLongestPalindromicSubs:


    @pytest.mark.parametrize("input, expected", [
        ("babad", "bab"),
        ("a", "a"),
        ("abcda", "a"),
        ("abacab", "bacab"),
        ("", "")
    ])
    def test_longest_palindrome(self, input, expected):
        assert LongestPalindromicSubs().longest_palindrome(input) == expected

