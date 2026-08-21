# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prevGroupLast = dummy

        while True:

            left = k
            curr = prevGroupLast.next
            stack = []
            while curr and left > 0:
                stack.append(curr)
                curr = curr.next
                left -= 1

            if left != 0:
                break

            groupNext = stack[-1].next

            curr = prevGroupLast
            while stack:
                curr.next = stack.pop()
                curr = curr.next

            curr.next = groupNext
            prevGroupLast = curr

        return dummy.next


            
        