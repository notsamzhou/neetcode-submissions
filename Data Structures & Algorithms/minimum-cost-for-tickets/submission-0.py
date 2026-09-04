class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i < 0:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = float("inf")

            for d, c in zip([1, 7, 30], costs):
                j = i

                # Find last travel day not covered by this pass
                while j >= 0 and days[i] - days[j] < d:
                    j -= 1

                dp[i] = min(dp[i], c + dfs(j))

            return dp[i]

        return dfs(len(days) - 1)