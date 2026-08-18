class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        M, N = len(obstacleGrid), len(obstacleGrid[0])

        cache = {}
        def dp(i, j):

            if not 0 <= i < M or not 0 <= j < N or obstacleGrid[i][j] == 1:
                return 0

            if (i, j) == (0, 0):
                return int(obstacleGrid[0][0] == 0)

            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
            return cache[(i, j)]

        return dp(M - 1, N - 1)

            
        