# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        prev = None
        curr = head
        idx = 0
        while curr and idx < length // 2:
            idx += 1
            prev = curr
            curr = curr.next
        if length % 2:
            prev = curr
            curr = curr.next

        prev.next = None

        

        # reverse from curr till the end
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        
        rev_head = prev

        idx = 0
        curr = head
        rev_curr = rev_head
        while curr and rev_curr and idx < length // 2:
            curr_temp = curr.next
            rev_temp = rev_curr.next

            curr.next = rev_curr
            rev_curr.next = curr_temp

            curr = curr_temp
            rev_curr = rev_temp
            idx += 1
        