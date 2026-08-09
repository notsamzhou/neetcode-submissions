# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        second = head
        for i in range(n):
            second = second.next

        prev = None
        curr = head

        while second is not None:
            prev = curr
            curr = curr.next
            second = second.next


        if prev:
            prev.next = curr.next
            curr.next = None
            return head

        else:
            return head.next


        