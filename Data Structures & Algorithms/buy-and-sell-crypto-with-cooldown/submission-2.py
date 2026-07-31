class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        cache = {}
        def dp(i, holding):

            if i < 0:
                return -math.inf if holding else 0


            if (i, holding) in cache:
                return cache[(i, holding)]
            if holding:
                cache[(i, holding)] = max(dp(i - 1, True), dp(i - 2, False) - prices[i])

            else:
                cache[(i, holding)] = max(dp(i - 1, False), dp(i - 1, True) + prices[i])


            return cache[(i, holding)]

        return dp(len(prices) - 1, False)



        