class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # A 2d array, with N rows and M + 1 columns, init with -1's
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for _ in range(N)]
        
        for i in range(N):
            dp[i][0] = 0

        for c in range(M):
            dp[0][c] = profit[0] if weight[0] <= c else 0

        for i in range(1, N):
            for c in range(1, M+1):
                skip = dp[i-1][c]

                include = 0
                if c - weight[i] >= 0:

                    include = profit[i] + dp[i-1][c-weight[i]]
                
                dp[i][c] = max(skip, include)

        return dp[N-1][M]



