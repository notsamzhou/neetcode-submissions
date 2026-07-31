class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)

        cache = {}
        def helper(i):
            if i < 0:
                return True

            if i in cache:
                return cache[i]

            res = False
            for word in wordDict:
                start = i - len(word) + 1
                if start < 0:
                    continue

                for j in range(len(word)):
                    if word[j] != s[start + j]:
                        break

                    if j == len(word) - 1:
                        res = res or helper(i - len(word))

            cache[i] = res
            return res

        return helper(len(s) - 1)

        