class HashTable:
    class ListNode:
        def __init__(self, key = None, value = None):
            self.key = key
            self.value = value
            self.next = None

        

    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.size = 0
        


    def insert(self, key: int, value: int) -> None:
        bucket = key % self.capacity
        if not self.arr[bucket]:
            self.arr[bucket] = self.ListNode()
            entry = self.ListNode(key, value)
            self.arr[bucket].next = entry
            self.size += 1

        else:
            prev = self.arr[bucket]
            curr = prev.next
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                
                prev = curr
                curr = curr.next

            prev.next = self.ListNode(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        bucket = key % self.capacity
        if not self.arr[bucket]:
            return -1

        curr = self.arr[bucket].next
        while curr:
            if curr.key == key:
                return curr.value

            curr = curr.next
        
        return -1


    def remove(self, key: int) -> bool:
        bucket = key % self.capacity
        if not self.arr[bucket]:
            return False

        prev = self.arr[bucket]
        curr = prev.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                self.size -= 1
                return True

            prev = curr
            curr = curr.next
        
        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        new_arr = [None] * (self.capacity * 2)
        new_cap = self.capacity * 2

        for i in range(self.capacity):
            if self.arr[i]:
                curr = self.arr[i].next

                while curr: # through original chain

                    if not new_arr[curr.key % new_cap]:
                        new_arr[curr.key % new_cap] = self.ListNode()

                    new_prev = new_arr[curr.key % new_cap]
                    new_curr = new_prev.next
                    while new_curr:
                        new_prev = new_curr
                        new_curr = new_curr.next

                    new_prev.next = self.ListNode(curr.key, curr.value)

                    curr = curr.next

        self.capacity = new_cap
        self.arr = new_arr


