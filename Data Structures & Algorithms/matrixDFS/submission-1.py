class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def helper(grid, r, c, visited):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == 1:
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            cnt = 0
            visited.add((r, c))

            for nr, nc in [(r -1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                cnt += helper(grid, nr, nc, visited)

            visited.remove((r, c))
            return cnt

        return helper(grid, 0, 0, set())
        