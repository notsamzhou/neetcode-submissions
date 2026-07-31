class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None
class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None


    def isEmpty(self) -> bool:
        return not self.head
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        removed = self.tail
        
        self.tail = removed.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return removed.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        removed = self.head
        self.head = removed.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed.val
