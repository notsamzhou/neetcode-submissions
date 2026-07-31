class MinHeap:
    
    def __init__(self):
        self.heap = []
        

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)


    def pop(self) -> int:
        if not self.heap:
            return -1

        if len(self.heap) == 1:
            return self.heap.pop()

        self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1]
        res = self.heap.pop()

        self._sift_down(0)
        return res

        

    def top(self) -> int:
        return self.heap[0] if self.heap else -1

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _sift_up(self, i):
        p = self._parent(i)
        while i != 0 and self.heap[p] > self.heap[i]:
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p
            p = self._parent(i)

    def _sift_down(self, i):
        l = self._left_child(i)
        r = self._right_child(i)

        while l < len(self.heap):

            if r < len(self.heap) and self.heap[r] < self.heap[l]:
                l, r = r, l
            
            if self.heap[i] <= self.heap[l]:
                break

            self.heap[i], self.heap[l] = self.heap[l], self.heap[i]

            i = l
            l = self._left_child(i)
            r = self._right_child(i)


            


        

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums

        for i in range(len(self.heap)-1, -1, -1):
            self._sift_down(i)

        
        