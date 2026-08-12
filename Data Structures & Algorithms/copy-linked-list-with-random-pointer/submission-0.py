"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        random_to_parents = dict()

        dummy_head = Node(-101)
        curr = head
        copy_curr = dummy_head


        copies = []
        i = 0
        while curr:

            copied = Node(curr.val)
            copy_curr.next = copied
            copies.append(copied)

            if curr.random is not None:
                if curr.random not in random_to_parents:
                    random_to_parents[curr.random] = []
                random_to_parents[curr.random].append(i)

            copy_curr = copy_curr.next
            curr = curr.next
            i += 1

        curr = head
        copy_curr = dummy_head.next
        i = 0
        while curr:

            if curr in random_to_parents:
                for p in random_to_parents[curr]:
                    copies[p].random = copy_curr


            copy_curr = copy_curr.next
            curr = curr.next
            i += 1

        return dummy_head.next


        

        

        