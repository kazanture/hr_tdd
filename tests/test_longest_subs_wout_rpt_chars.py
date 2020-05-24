import pytest
from leetcode_tdd.longest_subs_wout_rpt_chars import LongestSubsWOutRpt


class TestLongestSubs:

    @pytest.mark.parametrize('input_str, expected', [
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("bbbbb", 1),
        ("aab", 2),
        ("dvdf", 3),
        ("jbpnbwwd", 4),
        ("aabaab!bb", 3)
    ])
    def test_length_of_longest_substring(self, input_str, expected):
        assert LongestSubsWOutRpt.length_of_longest_substring(input_str) == expected
