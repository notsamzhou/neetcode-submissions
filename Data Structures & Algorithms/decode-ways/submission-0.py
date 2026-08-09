class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dp(i):
            if i < 0:
                return 1

            if i in cache:
                return cache[i]

            digit = int(s[i])

            if i == 0 and int(s[i]) != 0:
                return 1
            if i == 0 and int(s[i]) == 0:
                return 0

            if 0 < digit <= 6:
                
                if s[i-1] == "1" or s[i -1] == "2":
                    res = dp(i - 2) + dp(i - 1)
                else:
                    res = dp(i - 1)

            if 7 <= digit:
                if s[i-1] == "1":
                    res = dp(i - 2) + dp(i - 1)
                else:
                    res = dp(i - 1)

            if digit == 0:
                if s[i-1] == "1" or s[i -1] == "2":
                    res = dp(i - 2)
                else:
                    res = 0

            cache[i] = res
            print(i, res)
            return cache[i]

        return dp(len(s) - 1)


        