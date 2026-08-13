class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:


        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    
                    for ni, nj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                            res += 1

                        elif grid[ni][nj] == 0:
                            res += 1

        return res
        