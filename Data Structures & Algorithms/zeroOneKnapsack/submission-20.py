class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)

        for i in range(capacity + 1):
            if i >= weight[0]:
                dp[i] = profit[0]

        for i in range(1, len(profit)):
            new_row = [dp[i] for i in range(capacity + 1)]
            for j in range(weight[i], capacity + 1):
                new_row[j] = max(dp[j], profit[i] + dp[j - weight[i]])

            dp = new_row

        
        return dp[capacity]
