class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        M, N = len(heights), len(heights[0])
        visit_pc = set()
        visit_al = set()
        def dfs(r, c, visit):

            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < M and 0 <= nc < N and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    dfs(nr, nc, visit)

        for r in range(M):
            visit_pc.add((r, 0))
            dfs(r, 0, visit_pc)
            visit_al.add((r, N - 1))
            dfs(r, N-1, visit_al)

        for c in range(N):
            visit_pc.add((0, c))
            dfs(0, c, visit_pc)
            visit_al.add((M - 1, c))
            dfs(M - 1, c, visit_al)

        res = []
        for r in range(M):
            for c in range(N):
                if (r, c) in visit_pc and (r, c) in visit_al:
                    res.append((r, c))


        return res