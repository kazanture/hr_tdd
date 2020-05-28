import pytest

from leetcode_tdd.palindrome_number import PalindromeNumber


class TestPalindromeNumber:
    @pytest.mark.parametrize("number, expected", [
        (121, True),
        (1, True),
        (11, True),
        (-121, False),
        (12, False),
        (1212, False),
        (10, False),
        (313, True),
        (1001, True),
        (1000021, False)
    ])
    def test_is_palindrome(self, number, expected):
        assert PalindromeNumber().is_palindrome(number) == expected



    @pytest.mark.parametrize("number, expected", [
        (121, 3),
        (1, 1),
        (11, 2),
        (-121, 3),
        (12, 2),
        (1212, 4),
        (10, 2),
        (313, 3),
        (1001, 4),
        (1000021, 7),
        (0, 1)
    ])
    def test_get_number_of_digits(self, number, expected):
        assert PalindromeNumber().get_number_of_digits(number) == expected