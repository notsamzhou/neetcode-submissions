class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.nxt = None
        self.prev = None
        self.prevMin = None

class MinStack:

    def __init__(self):
        self.topNode = None
        self.minNode = None

    def push(self, val: int) -> None:
        
        if not self.topNode:
            self.topNode = ListNode(val)
            self.minNode = self.topNode

        else:
            newNode = ListNode(val)

            self.topNode.nxt = newNode
            newNode.prev = self.topNode
            self.topNode = self.topNode.nxt
            if val <= self.minNode.val:
                self.topNode.prevMin = self.minNode
                self.minNode = self.topNode
        

    def pop(self) -> None:
        
        toPop = self.topNode
        if self.minNode is toPop:
            self.minNode = toPop.prevMin

        self.topNode = toPop.prev
        if self.topNode:
            self.topNode.nxt = None

        return toPop.val
        
        

    def top(self) -> int:
        return self.topNode.val
        

    def getMin(self) -> int:
        return self.minNode.val

        
