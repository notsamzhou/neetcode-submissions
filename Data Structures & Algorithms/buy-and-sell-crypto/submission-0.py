class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        suffix_max = [prices[-1]] * len(prices)
        for i in range(len(prices) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], prices[i])

        res = 0
        for i in range(len(prices) - 2, -1, -1):
            res = max(suffix_max[i] - prices[i], res)

        return res