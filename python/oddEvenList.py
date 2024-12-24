from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        oddHead = head
        evenHead = head.next
        currOdd = oddHead
        currEven = evenHead

        while currEven and currEven.next:
            currOdd.next = currEven.next
            currOdd = currOdd.next

            currEven.next = currOdd.next
            currEven = currEven.next

        currOdd.next = evenHead
        return oddHead
