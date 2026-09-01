class ListNode:
    def __init__(self, key: int = -1, val: int = -1, prev: ListNode = None, next: ListNode = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0

        self.keyMap = dict()

        self.listHead = None
        self.listTail = None
        

    def get(self, key: int) -> int:

        if key in self.keyMap:

            node = self.keyMap[key]

            if node is not self.listHead:
                node.prev.next = node.next

                if node is not self.listTail:
                    node.next.prev = node.prev

                else:
                    self.listTail = node.prev

                node.prev = None
                node.next = self.listHead
                self.listHead.prev = node
                self.listHead = node

            return node.val

        return -1

        

    def put(self, key: int, value: int) -> None:

        if self.used == 0:
            node = ListNode(key, value, None, None)
            self.keyMap[key] = node
            self.listHead = node
            self.listTail = node
            self.used = 1

        elif key in self.keyMap:

            node = self.keyMap[key]
            node.val = value

            if node is not self.listHead:

                node.prev.next = node.next

                if node is not self.listTail:
                    node.next.prev = node.prev

                else:
                    self.listTail = node.prev

                node.prev = None
                node.next = self.listHead
                self.listHead.prev = node
                self.listHead = node

        else:
            node = ListNode(key, value, None, None)
            self.keyMap[key] = node

            if self.used == self.capacity:
                oldNode = self.listTail
                self.listTail = oldNode.prev

                if self.listTail is not None:
                    self.listTail.next = None

                if self.listTail is None:
                    self.listHead = None

                oldNode.prev = None

                del self.keyMap[oldNode.key]

            else:
                self.used += 1

            if self.listHead:
                self.listHead.prev = node
                node.next = self.listHead
                self.listHead = node

            else:
                self.listTail = node
                self.listHead = node




        
