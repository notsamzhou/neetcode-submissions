class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def valid_queen(i, j, queens):
            for queen in queens:
                if i == queen[0]:
                    return False

                if j == queen[1]:
                    return False

                if abs(queen[0] - i) == abs(queen[1] - j):
                    return False

            return True

        res = []
        queens = []
        def backtrack(i, queens):
            if i == n:
                curr = []
                for (i, j) in queens:
                    curr.append("." * j + "Q" + "." * (n - j - 1))
                
                res.append(curr)
                return

            for j in range(n):
                if valid_queen(i, j, queens):
                    queens.append([i, j])
                    backtrack(i + 1, queens)
                    queens.pop()


        backtrack(0, queens)
        return res
        