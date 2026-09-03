class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        def dfs(i, j):
            if not 0 <= i < M or not 0 <= j < N or grid[i][j] != 1:
                return

            island1.add((i, j))

            grid[i][j] = 2

            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                dfs(ni, nj)

        island1 = set()
        found = False
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

            if found:
                break
                

        queue = deque(list(island1))
        res = 0
        visited = set()
        while queue:

            
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ni < M and 0 <= nj < N:

                        if grid[ni][nj] == 1:
                            return res

                        elif grid[ni][nj] == 0 and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            queue.append((ni, nj))

            res += 1
        