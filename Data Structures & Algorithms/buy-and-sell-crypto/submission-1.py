class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        suffix_max = prices[-1]
        res = 0

        for i in range(len(prices) - 2, -1, -1):
            suffix_max = max(suffix_max, prices[i])
            res = max(suffix_max - prices[i], res)


        return res