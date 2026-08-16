class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # dp[i][j] = longest increasing path ending at i, j

        M, N = len(matrix), len(matrix[0])
        cache = {}
        def dp(i, j):

            if (i, j) in cache:
                return cache[(i, j)]

            res = 0
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not (0 <= ni < M and 0 <= nj < N):
                    continue

                if matrix[ni][nj] <= matrix[i][j]:
                    continue

                res = max(res, dp(ni, nj))

            res += 1

            cache[(i, j)] = res

            return res

        maximum = 0
        for i in range(M):
            for j in range(N):
                maximum = max(maximum, dp(i, j))

        print(cache)

        return maximum
                

        