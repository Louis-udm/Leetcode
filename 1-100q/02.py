"""NO.2 题目来源于 LeetCode 上第 2 号问题：两数相加。
题目难度为 Medium，目前通过率为 33.9%. 给出两个 **非空** 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。您可以假设除了数字 0 之外，
这两个数都不会以 0 开头。
https://zhenyu0519.github.io/2020/06/06/lc02/
"""

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_from_list(arr: list) -> Optional[ListNode]:
        head: Optional[ListNode] = None
        pre: Optional[ListNode] = None
        for i, it in enumerate(arr):
            node = ListNode(it)
            if i == 0:
                head = node
                pre = node
            if i > 0:
                pre.next = node
                pre = node
        return head

    def copy(self):
        head: Optional[ListNode] = None
        if self:
            p = self
            head = ListNode(p.val)
            cur = head
            while p.next:
                p = p.next
                cur.next = ListNode(p.val)
                cur = cur.next
        return head

    def __str__(self):
        p = self
        s = ""
        while p:
            s += f"{p.val} -> "
            p = p.next
        return s[:-4]


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = cur = ListNode("inf")
    carry = 0
    while l1 and l2:
        carry, val = divmod(l1.val + l2.val + carry, 10)
        node = ListNode(val)
        cur.next = node
        cur, l1, l2 = cur.next, l1.next, l2.next
    cur.next = l1.copy() if l1 else l2.copy()
    while carry and cur.next:
        carry, val = divmod(cur.next.val + carry, 10)
        cur.next.val = val
        cur = cur.next
    if carry:
        cur.next = ListNode(carry)
    return head.next


a = ListNode.create_from_list([2, 4, 8, 9])
print(a)
b = ListNode.create_from_list([5, 6, 4])
print(b)
print(addTwoNumbers(a, b))
print(a)
print(b)
