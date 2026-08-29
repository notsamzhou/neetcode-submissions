class Solution:
    def integerBreak(self, n: int) -> int:

        if n == 2:
            return 1

        if n == 3:
            return 2

        cache = {}
        def dp(m):

            if m == 1:
                return 1
            
            if m == 2:
                return 2


            if m in cache:
                return cache[m]

            res = m
            for i in range(1, m):
                res = max(res, i * dp(m - i))


            cache[m] = res

            return res

        return dp(n)


        