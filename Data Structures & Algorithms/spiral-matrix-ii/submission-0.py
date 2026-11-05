class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:


        res = [[1] * n for _ in range(n)]

        i = 0
        j = 0
        M, N = n, n

        curr = 1

        while i < M:
            for nj in range(j, N):
                res[i][nj] = curr
                curr += 1

            for ni in range(i + 1, M):
                res[ni][N - 1] = curr
                curr += 1

            for nj in range(N - 2, j - 1, -1):
                res[M - 1][nj] = curr
                curr += 1

            for ni in range(M - 2, i, -1):
                res[ni][j] = curr
                curr += 1

            i, j = i + 1, j + 1
            M, N = M - 1, N - 1

        return res

        