class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        dp = [0] * (capacity + 1)


        for i in range(1, capacity + 1):

            for j in range(len(profit)):
                if i - weight[j] >= 0:
                    dp[i] = max(dp[i], profit[j] + dp[i - weight[j]])

        return dp[capacity]

