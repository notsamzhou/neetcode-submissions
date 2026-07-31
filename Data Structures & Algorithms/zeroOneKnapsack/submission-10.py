class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity
        dp = [[0] * (m + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0
        for c in range(m + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0] 

        for i in range(1, n):
            for c in range(1, m + 1):
                skip = dp[i-1][c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i-1][c - weight[i]]
                dp[i][c] = max(include, skip)

        return dp[n-1][m]


