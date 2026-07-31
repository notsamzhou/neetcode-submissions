class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N= len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(i, j):
            if not (0 <= i < M and 0 <= j < N) or (i, j) in visit or grid[i][j] == -1:
                return

            visit.add((i, j))
            q.append((i, j))

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))

        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                addCell(i - 1, j)
                addCell(i, j - 1)
                addCell(i + 1, j)
                addCell(i, j + 1)

            dist += 1