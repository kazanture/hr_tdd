import pytest
from sandbox.string_to_integer import StringToInteger

class TestStringToInteger:


    @pytest.mark.parametrize("str_num, expected", [
        ("42", 42),
        ("      42", 42),
        ("   -12", -12),
        ("    321 skghdsjhg", 321),
        ("   ", 0),
        ("  sdgf", 0),
        ("  -99999999999999999", -2147483648),
        ("  76347267846237462", 2147483647),
        ("  000", 0),
        ("  +", 0),
        ("  -", 0),
        ("  +100", 100),
    ])
    def test_my_atoi(self,str_num, expected):
        assert StringToInteger().my_atoi(str_num) == expected
