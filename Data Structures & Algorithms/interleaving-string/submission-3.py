class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}
        def dp(i, j):
            if i < 0 and j < 0:
                return True
            
            if (i, j) in cache:
                return cache[(i, j)]

            res = False
            if i >= 0 and s3[i + j +1] == s1[i] and dp(i - 1, j):
                res = True

            if j >= 0 and s3[i + j + 1] == s2[j] and dp(i, j -1):
                res = True

            cache[(i, j)] = res
            return res

        return dp(len(s1) - 1, len(s2) - 1)