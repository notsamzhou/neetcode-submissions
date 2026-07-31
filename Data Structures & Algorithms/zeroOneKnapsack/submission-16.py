class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # A 2d array, with N rows and M + 1 columns, init with -1's
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.memoHelper(0, profit, weight, capacity, cache)

    def memoHelper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # Skip item i
        cache[i][capacity] = self.memoHelper(i + 1, profit, weight, capacity, cache)
        
        # Include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.memoHelper(i + 1, profit, weight, newCap, cache)
            # Compute the max
            cache[i][capacity] = max(cache[i][capacity], p)

        return cache[i][capacity]


