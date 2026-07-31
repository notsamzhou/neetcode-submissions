class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M, N = len(board), len(board[0])

        def dfs(i, j):
            if not (0 <= i < M and 0 <= j < N) or board[i][j] != "O":
                return

            board[i][j] = "T"

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)     


        for i in range(M):
            dfs(i, 0)
            dfs(i, N - 1)

        for j in range(N):
            dfs(0, j)
            dfs(M - 1, j)

        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "T":
                    board[i][j] = "O"
             