"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def build_from_string(self, string_number):
        prev_item = None
        for digit in reversed(string_number):
            if prev_item is None:
                self.val = int(digit)
                prev_item = self
                continue
            ln = ListNode(int(digit), None)
            prev_item.next = ln
            prev_item = ln

    def __str__(self):
        item = self
        res = str(item.val)
        while item.next:
            item = item.next
            res = str(item.val) + res
        return res


class LLIntegerAdder:

    @staticmethod
    def add_digits(d1, d2, d3):
        digit_sum = d1 + d2 + d3
        return digit_sum % 10, digit_sum // 10

    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        root.val, acc = LLIntegerAdder.add_digits(l1.val, l2.val, 0)
        prev_item = root
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            current_sum, acc = LLIntegerAdder.add_digits(l1.val, l2.val, acc)
            current_result = ListNode(current_sum)
            prev_item.next = current_result
            prev_item = current_result
        remaining_list = l1 if l1.next else l2
        while remaining_list.next:
            remaining_list = remaining_list.next
            current_sum, acc = LLIntegerAdder.add_digits(remaining_list.val, 0, acc)
            current_result = ListNode(current_sum)
            prev_item.next = current_result
            prev_item = current_result
        if acc > 0:
            prev_item.next = ListNode(acc)
        return root

