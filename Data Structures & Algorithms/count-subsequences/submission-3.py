class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = [[0] * len(s) for _ in range(len(t))]

        for i in range(len(t) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                
                if i == len(t) - 1:
                    dp[i][j] = 1 if t[i] == s[j] else 0

                    if j < len(s) - 1:
                        dp[i][j] += dp[i][j+1]

                else:
                    if j == len(s) - 1:
                        continue

                    
                    if dp[i + 1][j + 1] == 0:
                        continue

                    dp[i][j] = dp[i][j+1]

                    if s[j] == t[i]:
                        dp[i][j] = dp[i+1][j+1] + dp[i][j+1]
        return dp[0][0]
        # res = 0
        # for j in range(len(s)):
            
        #     if s[j] == t[0]:
        #         curr = 1
        #         for i in range(1, len(t)):
        #             if j + i >= len(s):
        #                 curr = 0
        #                 break

        #             curr *= dp[i][j+i]

        #         res += curr

        # return res


