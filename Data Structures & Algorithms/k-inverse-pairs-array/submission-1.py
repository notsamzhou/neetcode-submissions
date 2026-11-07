class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [1] + [0] * k

        for i in range(1, n + 1):
            dp2 = [0] * (k + 1)

            curr = 0
            for j in range(k + 1):
                curr += dp[j]

                if j >= i:
                    curr -= dp[j - i]

                dp2[j] = curr

            dp = dp2

        return dp[k] % 1000000007
