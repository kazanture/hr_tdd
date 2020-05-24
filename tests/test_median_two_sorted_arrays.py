import pytest
from leetcode_tdd.median_two_sorted_arrays import MedianTwoSortedArrays
class TestMedianTwoSortedArrays:

    @pytest.mark.parametrize("nums1, nums2, expected",[
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([1, 1, 1], [0], 1.0)
    ])
    def test_find_median_sorted_arrays(self, nums1, nums2, expected):
        assert MedianTwoSortedArrays.find_median_sorted_arrays(nums1, nums2) == expected
