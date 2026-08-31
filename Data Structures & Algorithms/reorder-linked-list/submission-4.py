# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 1 if head else 0


        prev = None
        curr = head
        while curr.next:
            length += 1
            prev = curr
            curr = curr.next

        half = length // 2
        prev = None
        curr = head
        idx = 0
        while idx < half:
            prev = curr
            curr = curr.next
            idx += 1

        if length % 2:
            prev = curr
            curr = curr.next
        
        prev.next = None

        # curr is the first of the second half

        prev = None
        # reverse the back half
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        rev_curr = prev
        curr = head


        for _ in range(half):
            tmp1, tmp2 = curr.next, rev_curr.next

            curr.next =  rev_curr
            rev_curr.next = tmp1

            curr, rev_curr = tmp1, tmp2

