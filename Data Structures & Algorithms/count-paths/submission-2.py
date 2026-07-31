class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = [[0] * n for _ in range(m)]
        def dfs(r, c):
            if r < 0 or c < 0:
                return 0
            if r == 0 and c == 0:
                return 1

            if cache[r][c]:
                return cache[r][c]

            cache[r][c] = dfs(r - 1, c) + dfs(r, c - 1)

            return cache[r][c]

        return dfs(m-1, n-1)

        