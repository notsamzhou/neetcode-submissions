class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):

            grid[i][j] = '0'

            for r, c in [(i-1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1':
                    dfs(r, c)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1

                    dfs(i, j)

        return count
        