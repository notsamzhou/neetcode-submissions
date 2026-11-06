class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        cache = {}
        def dp(i):
            if i == 1:
                return k

            if i == 2:
                return k * k

            if i in cache:
                return cache[i]

            cache[i] = (k - 1) * dp(i - 1) + (k - 1) * dp(i - 2)
            return cache[i]

        return dp(n)