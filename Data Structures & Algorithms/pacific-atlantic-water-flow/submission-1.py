class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        M, N = len(heights), len(heights[0])
        visited = set()
        visit_pc = set()
        visit_al = set()
        def dfs(r, c):

            visited.add((r, c))

            if r == 0:
                visit_pc.add((r, c))
            if c == 0:
                visit_pc.add((r, c))

            if r == M - 1:
                visit_al.add((r, c))
            if c == N - 1:
                visit_al.add((r, c))



            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < M and 0 <= nc < N and heights[nr][nc] <= heights[r][c]:
                    
                    if (nr, nc) not in visited:
                        dfs(nr, nc)

                    if (nr, nc) in visit_al:
                        visit_al.add((r, c))
                    if (nr, nc) in visit_pc:
                        visit_pc.add((r, c))

        for r in range(M):
            for c in range(N):
                dfs(r, c)


        res = []
        for r in range(M):
            for c in range(N):
                if (r, c) in visit_pc and (r, c) in visit_al:
                    res.append((r, c))


        return res