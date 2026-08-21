class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:


        shortest = [[math.inf] * len(grid[0]) for _ in range(len(grid))]
        shortest[0][0] = grid[0][0]

        heap = [(grid[0][0], (0, 0))]

        while heap:
            dist, (r, c) = heapq.heappop(heap)

            if dist > shortest[r][c]:
                continue

            if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
                return dist

            if r + 1 < len(grid):
                if dist + grid[r+1][c] < shortest[r+1][c]:
                    shortest[r+1][c] = dist + grid[r+1][c]
                    heapq.heappush(heap, (shortest[r+1][c], (r + 1, c)))

            if c + 1 < len(grid[0]):
                if dist + grid[r][c+1] < shortest[r][c+1]:
                    shortest[r][c+1] = dist + grid[r][c+1]
                    heapq.heappush(heap, (shortest[r][c+1], (r, c+1)))

        return shortest[len(grid) - 1][len(grid[0]) - 1]
        