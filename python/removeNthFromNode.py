from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        pos = length - n
        counter = 0

        if pos == 0:
            return head.next
        else:
            prev = None
            curr = head
            while counter < pos:
                prev = curr
                curr = curr.next
                counter += 1

            prev.next = curr.next
            return head
