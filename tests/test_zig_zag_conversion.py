import pytest
from leetcode_tdd.zig_zag_conversion import ZigZagConversion
class TestZigZagConversion:
    @pytest.mark.parametrize("input_str, num_rows, expected", [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("AB", 1, "AB")
    ])
    def test_convert(self, input_str, num_rows, expected):
        assert ZigZagConversion().convert(input_str, num_rows) == expected
