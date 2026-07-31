# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()
        curr_node = head

        h = []
        for l in lists:
            heapq.heappush(h, (l.val, NodeWrapper(l)))

        while h:
            wrapper = heapq.heappop(h)
            next_node = wrapper[1].node

            curr_node.next = next_node
            curr_node = curr_node.next

            next_node = next_node.next
            if next_node:
                heapq.heappush(h, (next_node.val, NodeWrapper(next_node)))

            curr_node.next = None

        return head.next


        