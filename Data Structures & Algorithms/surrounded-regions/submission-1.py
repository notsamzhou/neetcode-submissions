class Solution:
    def solve(self, board: List[List[str]]) -> None:

        M, N = len(board), len(board[0])

        def dfs(r, c):

            if not 0 <= r < M or not 0 <= c < N or board[r][c] != "O":
                return

            board[r][c] = "T"

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                dfs(nr, nc)


        for r in range(M):
            dfs(r, 0)
            dfs(r, N - 1)

        for c in range(N):
            dfs(0, c)
            dfs(M - 1, c)

        for r in range(M):
            for c in range(N):
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "T":
                    board[r][c] = "O"
            
        