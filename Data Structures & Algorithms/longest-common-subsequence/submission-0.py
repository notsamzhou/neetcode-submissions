class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        cache = {}
        def lcs_helper(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i < 0 or j < 0:
                return 0

            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + lcs_helper(i - 1, j-1)

            else:
                cache[(i, j)] = max(lcs_helper(i - 1, j), lcs_helper(i, j-1))

            return cache[(i, j)]

        return lcs_helper(n - 1, m - 1)