# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLinkedListSize(self, head: Optional[ListNode]) -> int:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        return size

    def deleteElement(
        self, position: int, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if position == 0:
            return head.next

        curr = head
        for i in range(position - 1):
            if curr is None:
                return head
            curr = curr.next

        if curr is None or curr.next is None:
            return head
        curr.next = curr.next.next
        return head

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        linkedListSize = self.getLinkedListSize(head)
        targetPosition = linkedListSize // 2
        self.deleteElement(targetPosition, head)
        return head
