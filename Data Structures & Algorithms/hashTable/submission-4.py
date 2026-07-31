class ListNode:
    def __init__(self, key = None, value = None, next_node = None):
        self.key = key
        self.value = value
        self.next = next_node
class HashTable:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.size = 0



    def insert(self, key: int, value: int) -> None:
        h = key % self.capacity

        if not self.arr[h]:
            self.arr[h] = ListNode(key, value)
            self.size += 1
            if self.size >= 0.5 * self.capacity:
                self.resize()
            return

        else:
            prev = None
            curr = self.arr[h]
            while curr:
                
                if curr.key == key:
                    curr.value = value
                    return

                prev = curr
                curr = curr.next

            prev.next = ListNode(key, value)
            self.size += 1         

            if self.size >= 0.5 * self.capacity:
                self.resize()


    def get(self, key: int) -> int:
        h = key % self.capacity

        if not self.arr[h]:
            return -1

        else:
            prev = None
            curr = self.arr[h]
            while curr:
                
                if curr.key == key:
                    return curr.value

                prev = curr
                curr = curr.next

        return -1


    def remove(self, key: int) -> bool:
        h = key % self.capacity

        if not self.arr[h]:
            return False

        else:
            prev = None
            curr = self.arr[h]
            while curr:
                
                if curr.key == key:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.arr[h] = curr.next
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
        self.capacity = self.capacity * 2
        old_arr = self.arr
        self.arr = [None] * self.capacity
        self.size = 0

        for i in range(self.capacity // 2):
            curr = old_arr[i]
            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next

        


