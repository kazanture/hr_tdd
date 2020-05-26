import pytest
from sandbox.two_sum import  TwoSum

class TestTwoSum:

    @pytest.mark.parametrize("arr, target, expected",[
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 3, 2, 6], 9, [0, 3])
    ])
    def test_two_sum(self, arr, target, expected):
        assert TwoSum().two_sum(arr, target) == expected
