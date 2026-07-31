class LinkNode:

    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None


    
    def get(self, index: int) -> int:
        i = 0
        current = self.head
        while current is not None and i != index:
            current = current.next
            i += 1

        if current is None:
            return -1

        return current.value

        

    def insertHead(self, val: int) -> None:

        new_head = LinkNode(val)
        new_head.next = self.head

        if self.head is None:
            self.tail = new_head

        self.head = new_head
        

    def insertTail(self, val: int) -> None:

        new_tail = LinkNode(val)
        if self.tail is None:
            self.head = new_tail
        else:
            self.tail.next = new_tail

        self.tail = new_tail
        

    def remove(self, index: int) -> bool:
        prev = None
        current = self.head
        i = 0
        while i != index and current is not None:
            prev = current
            current = current.next
            i += 1

        if current is None:
            return False

        if current.next is None:
            self.tail = prev

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

        

        return True
        

    def getValues(self) -> List[int]:
        vals = []
        current = self.head

        while current is not None:
            vals.append(current.value)
            current = current.next

        return vals
        
