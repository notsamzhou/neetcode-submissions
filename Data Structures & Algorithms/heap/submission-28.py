class MinHeap:
    
    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self._heapify_up(len(self.arr) - 1)


    def pop(self) -> int:
        if self.arr:
            smallest = self.arr[0]

            last = self.arr.pop(-1)
            
            if self.arr:
                self.arr[0] = last

                self._heapify_down(0)
                
            return smallest

        else:
            return -1
        

    def top(self) -> int:
        if self.arr:
            return self.arr[0]
        else:
            return -1
        

    def heapify(self, nums: List[int]) -> None:
        self.arr = nums
        for i in reversed(range(len(nums) // 2)):
            self._heapify_down(i)

        print(self.arr)

    
    def _heapify_down(self, idx):
        child = 2 * idx + 1
        while child < len(self.arr):
            if child + 1 < len(self.arr) and self.arr[child] > self.arr[child + 1]:
                child += 1

            if self.arr[idx] > self.arr[child]:
                temp = self.arr[idx]
                self.arr[idx] = self.arr[child]
                self.arr[child] = temp

                idx = child
                child = idx * 2 + 1
            else:
                return

    def _heapify_up(self, idx):
        parent = (idx - 1) // 2


        while self.arr[parent] > self.arr[idx] and idx > 0:
            temp = self.arr[idx]
            self.arr[idx] = self.arr[parent]
            self.arr[parent] = temp
            idx = parent
            parent = (idx - 1) // 2



        
        