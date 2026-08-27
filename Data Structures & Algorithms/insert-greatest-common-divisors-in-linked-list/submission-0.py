# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a, b):
            while b > 0:
                a, b = b, a % b

            return a

        dummy = head

        curr = head
        while curr and curr.next:
            val1 = curr.val
            val2 = curr.next.val

            val3 = gcd(val1, val2)

            temp = curr.next

            curr.next = ListNode(val3)
            curr.next.next = temp

            curr = temp

        return dummy

        