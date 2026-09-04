class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cache = {}
        def helper(i, j):

            if i < 0:
                return True

            if j < 0:
                return False

            if (i, j) in cache:
                return cache[(i, j)]

            res = helper(i, j - 1)

            if s[i] == t[j]:
                res = res or helper(i - 1, j - 1)

            cache[(i, j)] = res
            return cache[(i, j)]

        return helper(len(s) - 1, len(t) - 1)
        