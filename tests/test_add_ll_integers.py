from leetcode_tdd.ll_integer_adder import ListNode, LLIntegerAdder
import pytest


def test_build_from_string():
    my_list = ListNode()
    my_list.build_from_string("123")

    assert my_list.val == 3
    assert my_list.next.val == 2
    assert my_list.next.next.val == 1


def test_to_string():
    l1 = ListNode()
    l1.build_from_string("342")

    assert str(l1) == "342"


@pytest.mark.parametrize('l1_str, l2_str, expect', [
    ("342", "465", "807"),
    ("8342", "465", "8807"),
    ("5", "5", "10")
])
def test_add_two_numbers(l1_str, l2_str, expect):
    l1 = ListNode()
    l1.build_from_string(l1_str)
    l2 = ListNode()
    l2.build_from_string(l2_str)

    res = LLIntegerAdder.add_two_numbers(l1, l2)
    assert str(res) == expect


@pytest.mark.parametrize('d1, d2, d3, expect', [
    (9, 9, 1, (9, 1)),
    (8, 5, 0, (3, 1)),
    (0, 0, 1, (1, 0))
])
def test_add_digits(d1, d2, d3, expect):
    assert LLIntegerAdder.add_digits(d1, d2, d3) == expect
