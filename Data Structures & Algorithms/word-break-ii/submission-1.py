class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        maxLen = max([len(word) for word in wordDict])

        # # dp(i) = OR_{i - maxLen < j <= i} dp(j-1) and s[j:i + 1] in wordDict

        # cache = {}
        # def dp(i):

        #     if i < 0:

        #         return True

        #     if i in cache:
        #         return cache[i]

        #     res = False
        #     for j in range(i - maxLen + 1, i + 1):

        #         if s[j:i + 1] in wordDict:

        #             res = res or dp(j - 1)

        #     cache[i] = res
        #     return cache[i]

        # return dp(len(s) - 1)

        res = []

        def helper(i, curr):

            if i == len(s):
                res.append(" ".join(curr))
                return

            for j in range(i, min(len(s), i + maxLen)):
                
                word = s[i:j + 1]
                if word in wordDict:
                    curr.append(word)
                    helper(j + 1, curr)
                    curr.pop()


            
        helper(0, [])

        return res


            