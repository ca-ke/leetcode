import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is not None:
            tail = None
            while head is not None:
                print(head.val)
                head = head.next
                tail = head
            if tail is not None:
                print(tail.val)
        return True


print(
    Solution().isPalindrome(
        ListNode(1, next=ListNode(2, next=ListNode(2, next=ListNode(1, next=None))))
    )
)
