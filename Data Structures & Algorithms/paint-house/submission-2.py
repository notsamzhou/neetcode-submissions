class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        cache = {}
        def dp(i, c):

            if i == len(costs):
                return 0

            if (i, c) in cache:
                return cache[(i, c)]
            best = math.inf
            for color in range(len(costs[0])):
                if c == color:
                    continue
                best = min(best, costs[i][c] + dp(i + 1, color))

            cache[(i, c)] = best
            return cache[(i, c)]

        return min(dp(0, 0), dp(0, 1), dp(0, 2))