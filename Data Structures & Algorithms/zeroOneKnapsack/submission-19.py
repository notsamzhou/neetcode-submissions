class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # A 2d array, with N rows and M + 1 columns, init with -1's
        N, M = len(profit), capacity
        dp = [0] * (M + 1)
        
        for c in range(M+1):
            dp[c] = profit[0] if weight[0] <= c else 0

        for i in range(1, N):
            row = [0] * (M + 1)
            for c in range(1, M+1):
                skip = dp[c]

                include = 0
                if c - weight[i] >= 0:

                    include = profit[i] + dp[c-weight[i]]
                
                row[c] = max(skip, include)

            dp = row

        return dp[M]



