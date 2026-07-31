class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfsHelper(0, profit, weight, capacity)

    def dfsHelper(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0

        # Skip item i
        maxProfit = self.dfsHelper(i + 1, profit, weight, capacity)

        # Include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfsHelper(i + 1, profit, weight, newCap)
            # Compute the max
            maxProfit = max(maxProfit, p)

        return maxProfit


