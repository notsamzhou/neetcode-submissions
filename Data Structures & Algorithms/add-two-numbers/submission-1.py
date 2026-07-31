# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        curr = result
        carry = 0

        while l1 and l2:

            val = l1.val + l2.val
            if carry:
                val += 1

            carry = 0
            if val >= 10:
                carry = 1
                val = val % 10

            new_node = ListNode(val, None)
            curr.next = new_node
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val
            if carry:
                val += 1

            carry = 0
            if val >= 10:
                carry = 1
                val = val % 10

            new_node = ListNode(val, None)
            curr.next = new_node
            curr = curr.next

            l1 = l1.next

        while l2:
            val = l2.val
            if carry:
                val += 1

            carry = 0
            if val >= 10:
                carry = 1
                val = val % 10

            new_node = ListNode(val, None)
            curr.next = new_node
            curr = curr.next

            l2 = l2.next

        if carry:
            curr.next = ListNode(1, None)

        return result.next


        