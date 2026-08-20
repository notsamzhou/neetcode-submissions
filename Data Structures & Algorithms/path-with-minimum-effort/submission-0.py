class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        M, N = len(heights), len(heights[0])

        best = [[math.inf] * N for _ in range(M)]
        best[0][0] = 0
        effort = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        heap = [(0, 0, 0)] # edge weight, r, c

        while heap:
            weight, r, c = heapq.heappop(heap)

            if weight > best[r][c]:
                continue

            effort = max(effort, weight)

            if (r, c) == (M-1, N-1):
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < M and 0 <= nc < N):
                    if abs(heights[r][c] - heights[nr][nc]) < best[nr][nc]:
                        best[nr][nc] = abs(heights[r][c] - heights[nr][nc])
                        heapq.heappush(heap, (best[nr][nc], nr, nc))

        return effort

            


        