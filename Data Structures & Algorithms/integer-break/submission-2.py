class Solution:
    def integerBreak(self, n: int) -> int:


        cache = {}
        def dp(m):

            if m in cache:
                return cache[m]


            res = 0 if m == n else m
            for i in range(1, m):
                res = max(res, i * dp(m - i))


            cache[m] = res

            return res

        return dp(n)


        