class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        M, N = len(grid), len(grid[0])

        dist = [[math.inf] * N for _ in range(M)]
        dist[0][0] = grid[0][0]
        heap = [(grid[0][0], (0, 0))]
        visited = set()
        while heap:

            weight, (i, j) = heapq.heappop(heap)

            if (i, j) == (M - 1, N - 1):
                return weight

            if (i, j) in visited:
                continue

            visited.add((i, j))

            for ni, nj in ((i -1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < M and 0 <= nj < N:
                    w = max(weight, grid[ni][nj])
                    if dist[ni][nj] > w:
                        dist[ni][nj] = w
                        heapq.heappush(heap, (w, (ni, nj)))





        