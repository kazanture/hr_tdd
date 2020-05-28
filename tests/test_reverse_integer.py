import pytest
from leetcode_tdd.reverse_integer import ReverseInteger


class TestReverseInteger:
    @pytest.mark.parametrize("num, expected",[
        (123, 321),
        (5, 5),
        (-123, -321),
        (120, 21)
    ])
    def test_reverse(self, num, expected):
        assert ReverseInteger().reverse(num) == expected
