from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque([(0, 0, 0)])
        visited = set((0, 0))
        length = 0

        while queue:
            curr_len, r, c = queue.popleft()

            if (r, c) == (ROWS - 1, COLS - 1):
                return curr_len

            for (nr, nc) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] != 1:
                    visited.add((nr, nc))
                    queue.append((curr_len + 1, nr, nc))


        return -1
        