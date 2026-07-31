class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        stack = []
        stack.append((0, 0, False))

        res = 0
        while stack:

            r, c, to_pop  = stack.pop()

            if r == ROWS - 1 and c == COLS - 1:
                res += 1
                continue

            if to_pop:
                visit.remove((r, c))
            else:

                if (r, c) not in visit:
                    visit.add((r, c))    
                    stack.append((r, c, True))            

                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        if (min(r + dr, c + dc) < 0 or
                            r + dr == ROWS or c + dc == COLS or
                            (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                            continue
                            
                        stack.append((r + dr, c + dc, False))
                    




        return res
        