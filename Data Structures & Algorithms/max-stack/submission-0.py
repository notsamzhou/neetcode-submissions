class ListNode:
    def __init__(self, val = None, nxt = None, prev = None, active=False, order = 0):
        self.val = val
        self.nxt = nxt
        self.prev = prev
        self.active = active
        self.order = order

    def __lt__(self, other):
        return (self.val, self.order) < (other.val, other.order)

class MaxStack:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head

        self.order = 0
        self.maxHeap = []
        

    def push(self, x: int) -> None:

        node = ListNode(x, self.tail, self.tail.prev, True, self.order)
        self.order += 1
        self.tail.prev.nxt = node
        self.tail.prev = node

        heapq.heappush_max(self.maxHeap, node)
        

    def pop(self) -> int:
        if self.tail.prev is not self.head:
            node = self.tail.prev

            node.prev.nxt = self.tail
            self.tail.prev = node.prev
            node.active = False

            return node.val

        return -1
        

    def top(self) -> int:
        if self.tail.prev is not self.head:
            return self.tail.prev.val

        return -1
        

    def peekMax(self) -> int:

        while not self.maxHeap[0].active:
            heapq.heappop_max(self.maxHeap)

        if self.maxHeap:
            return self.maxHeap[0].val
        else:
            return -1
        

    def popMax(self) -> int:
        while self.maxHeap and not self.maxHeap[0].active:
            heapq.heappop_max(self.maxHeap)

        if self.maxHeap:
            node = heapq.heappop_max(self.maxHeap)
            node.active = False

            prev = node.prev
            nxt = node.nxt

            prev.nxt = nxt
            nxt.prev = prev
            return node.val

        else:
            return -1
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
