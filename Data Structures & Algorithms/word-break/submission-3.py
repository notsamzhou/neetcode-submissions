class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t, len(w))

        cache = {}
        def helper(i):
            if i < 0:
                return True

            if i in cache:
                return cache[i]

            res = False
            for j in range(1, t + 1):
                start = i - j + 1
                if start >= 0 and s[start: i + 1] in words:
                    res = res or helper(start - 1)
                    if res:
                        cache[i] = res
                        return res

                


            cache[i] = res
            return res

        return helper(len(s) - 1)
