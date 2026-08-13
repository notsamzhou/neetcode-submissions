class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(i, holding):

            if i < 0:
                return -float("inf") if holding else 0

            if (i, holding) in cache:
                return cache[(i, holding)]

            if holding:
                cache[(i, holding)] = max(dp(i - 1, False) - prices[i], dp(i - 1, True))

            if not holding:
                cache[(i, holding)] = max(dp(i - 1, True) + prices[i], dp(i - 1, False))

            return cache[(i, holding)]

        return dp(len(prices) - 1, False)
        