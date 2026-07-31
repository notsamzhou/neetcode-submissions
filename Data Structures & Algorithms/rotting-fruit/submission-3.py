class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        queue = deque()
        
        def addCell(i, j):
            if not (0 <= i < M and 0 <= j < N) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            queue.append((i, j))

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    queue.append((i, j))

        steps = 0
        while queue:
            for _ in range(len(queue)):

                i, j = queue.popleft()
                addCell(i - 1, j)
                addCell(i + 1, j)
                addCell(i, j - 1)
                addCell(i, j + 1)

            if queue:
                steps += 1

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1

        return steps

        