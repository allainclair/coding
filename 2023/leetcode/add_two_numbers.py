"""https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains
a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

e.g.
   2 -> 4 -> 3
   5 -> 6 -> 4
 + -----------
   7 -> 0 -> 8

   9 -> 9 -> 9
   9 -> 9 -> 9
 + -----------
   8 -> 9 -> 9 -> 1
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    carry = 0
    values = []

    while True:
        if l1 is None and l2 is not None:
            sum_ = l2.val + carry
            digit = sum_ % 10
            values.append(digit)
            carry = sum_ // 10
            l2 = l2.next
        elif l1 is not None and l2 is None:
            sum_ = l1.val + carry
            digit = sum_ % 10
            values.append(digit)
            carry = sum_ // 10
            l1 = l1.next
        elif l1 is not None and l2 is not None:
            sum_ = l1.val + l2.val + carry
            digit = sum_ % 10
            values.append(digit)
            carry = sum_ // 10
            l1 = l1.next
            l2 = l2.next
        elif l1 is None and l2 is None:
            if carry:
                values.append(carry)
            new_node = None
            while values:
                value = values.pop()
                node = ListNode(val=value)
                node.next = new_node
                new_node = node
            return new_node


def check_equal(list_: ListNode | None, expected_list: ListNode | None) -> bool:
    while True:
        if list_ is None and expected_list is not None:
            return False
        if list_ is not None and expected_list is None:
            return False
        if list_ is None and expected_list is None:
            return True
        if list_.val != expected_list.val:
            return False
        list_ = list_.next
        expected_list = expected_list.next


def main() -> None:
    n_1_1 = ListNode(3)
    n_1_2 = ListNode(4)
    n_1_3 = ListNode(2)
    n_1_3.next = n_1_2
    n_1_2.next = n_1_1

    n_2_1 = ListNode(4)
    n_2_2 = ListNode(6)
    n_2_3 = ListNode(5)
    n_2_3.next = n_2_2
    n_2_2.next = n_2_1

    expected_1 = ListNode(8)
    expected_2 = ListNode(0)
    expected_3 = ListNode(7)
    expected_3.next = expected_2
    expected_2.next = expected_1

    list_ = add_two_numbers(n_1_3, n_2_3)
    assert check_equal(list_, expected_3)

    n_1_1 = ListNode(9)
    n_1_2 = ListNode(9)
    n_1_3 = ListNode(9)
    n_1_3.next = n_1_2
    n_1_2.next = n_1_1

    n_2_1 = ListNode(9)
    n_2_2 = ListNode(9)
    n_2_3 = ListNode(9)
    n_2_3.next = n_2_2
    n_2_2.next = n_2_1

    expected_1 = ListNode(1)
    expected_2 = ListNode(9)
    expected_3 = ListNode(9)
    expected_4 = ListNode(8)
    expected_4.next = expected_3
    expected_3.next = expected_2
    expected_2.next = expected_1

    list_ = add_two_numbers(n_1_3, n_2_3)
    assert check_equal(list_, expected_4)


if __name__ == "__main__":
    main()
