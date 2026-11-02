class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n != 0:
            return 0

        if n == 0:
            return 1

        cache = {}
        cache[1] = x
        cache[0] = 1
        cache[2] = x * x
        def helper(i):
            if i == 0:
                return 1

            if i in cache:
                return cache[i]

            if i % 2:
                cache[i] = helper(i // 2) * helper(i // 2) * x

            else:
                cache[i] = helper(i // 2) * helper(i // 2)

            return cache[i]

        res = helper(abs(n))
        if n < 0:
            return 1 / res

        return res

            