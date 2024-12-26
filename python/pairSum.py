# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        maxSum = 0
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            maxSum = max(maxSum, firstHalf.val + secondHalf.val)
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return maxSum
