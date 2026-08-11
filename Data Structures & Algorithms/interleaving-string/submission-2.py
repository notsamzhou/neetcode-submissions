class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}
        def dp(i, j, k):
            if i < 0 and j < 0:
                return True
            
            if (i, j) in cache:
                return cache[(i, j)]

            res = False
            if i >= 0 and s3[k] == s1[i] and dp(i - 1, j, k-1):
                res = True

            if j >= 0 and s3[k] == s2[j] and dp(i, j -1, k - 1):
                res = True

            cache[(i, j)] = res
            return res

        return dp(len(s1) - 1, len(s2) - 1, len(s3) - 1)