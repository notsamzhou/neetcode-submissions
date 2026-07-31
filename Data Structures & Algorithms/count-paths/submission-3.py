class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prev = [1] * n
        dp = [0] * n


        for i in range(1, m):
            for j in range(n):

                dp[j] = prev[j]
                if j != 0:
                    dp[j] += dp[j-1]

                
            prev = dp
            dp = [0] * n
        return prev[-1]
