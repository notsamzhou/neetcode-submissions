class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, idx):
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) or (r, c) in visited:
                return False

            if word[idx] != board[r][c]:
                return False

            if idx == len(word) - 1:
                return True

            visited.add((r, c))

            if dfs(r - 1, c, idx + 1) or dfs(r + 1, c, idx + 1) or dfs(r, c - 1, idx + 1) or dfs(r, c + 1, idx + 1):
                return True

            visited.remove((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = set()
                if dfs(r, c, 0):
                    return True


        return False
        