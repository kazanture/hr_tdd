"""
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""


class TwoSum:

    def two_sum(self, arr, target):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == target:
                    return [i, j]
