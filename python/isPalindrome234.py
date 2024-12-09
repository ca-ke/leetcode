import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slowPointer, fastPointer = head, head
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next

        prev = None
        curr = slowPointer
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        firstHalf, secondHalf = head, prev
        while secondHalf:
            if firstHalf.val != secondHalf.val:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return True


print(
    Solution().isPalindrome(
        ListNode(1, next=ListNode(2, next=ListNode(2, next=ListNode(1, next=None))))
    )
)
