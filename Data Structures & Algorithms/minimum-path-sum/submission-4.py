class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        cache = {}
        
        def dp(i, j):

            if i < 0 or j < 0:
                return math.inf

            if (i, j) in cache:
                return cache[(i, j)]

            if i == 0 and j == 0:
                return grid[0][0]

            cache[(i, j)] = grid[i][j] + min(dp(i - 1, j), dp(i, j-1))

            return cache[(i, j)]

        return dp(len(grid)-1, len(grid[0])-1)