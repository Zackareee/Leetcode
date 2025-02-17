# 206. Reverse Linked List
import pytest
from typing import List, Optional
import math
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: "ListNode" = None


class Solution:
    # 0 ms | Beats 100.00%
    # 18.59 MB | Beats 79.55%

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None and head.next is not None:

            current = head
            next = head.next

            head.next = prev
            head = next
            prev = current
        if head is None:
            return head
        head.next = prev
        return head


@pytest.fixture
def init_linkedlist():
    five = ListNode(val=5, next=None)
    four = ListNode(val=4, next=five)
    three = ListNode(val=3, next=four)
    two = ListNode(val=2, next=three)
    one = ListNode(val=1, next=two)
    return one


def test_cases():
    five = ListNode(val=5, next=None)
    four = ListNode(val=4, next=five)
    three = ListNode(val=3, next=four)
    two = ListNode(val=2, next=three)
    one = ListNode(val=1, next=two)

    val = Solution()

    result: Optional[ListNode] = val.reverseList(one)

    assert result.val == 5
    assert result.next.val == 4
    assert result.next.next.val == 3
    assert result.next.next.next.val == 2
    assert result.next.next.next.next.val == 1


def test_cases2():

    val = Solution()

    result: Optional[ListNode] = val.reverseList(None)
