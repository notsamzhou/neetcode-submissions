class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.n = 1<<(len(nums)-1).bit_length()
        self.arr = [0] * (2 * self.n - 1)

        for i in range(len(nums)):
            self.arr[i + self.n - 1] = nums[i]

        self._build(0, 0, self.n)


    def _left_c(self, i):
        return 2 * i + 1

    def _right_c(self, i):
        return 2 * i + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _build(self, u, L, R):
        mid = (L + R) // 2
        lc = self._left_c(u)
        rc = self._right_c(u)

        if lc < self.n - 1:
            self._build(lc, L, mid)

        if rc < self.n - 1:
            self._build(rc, mid, R)

        if lc < len(self.arr) and rc < len(self.arr):
            self.arr[u] = self.arr[lc] + self.arr[rc]


    
    def update(self, index: int, val: int) -> None:

        u = index + self.n - 1
        self.arr[u] = val

        while u > 0:
            u = self._parent(u)
            self.arr[u] = self.arr[self._left_c(u)] + self.arr[self._right_c(u)]


    
    def query(self, L: int, R: int) -> int:
        return self.compute_sum(0, L, R + 1, 0, self.n)


    def compute_sum(self, u, L, R, i, j):

        if L <= i and j <= R:
            return self.arr[u]

        else:
            mid = (i + j) // 2
            if L >= mid:
                return self.compute_sum(self._right_c(u), L, R, mid, j)
            elif R <= mid:
                return self.compute_sum(self._left_c(u), L, R, i, mid)

            else:
                left_sum = self.compute_sum(self._left_c(u), L, R, i, mid)
                right_sum = self.compute_sum(self._right_c(u), L, R, mid, j)
                return left_sum + right_sum





