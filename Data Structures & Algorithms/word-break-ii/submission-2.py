class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        maxLen = max([len(word) for word in wordDict])

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


            