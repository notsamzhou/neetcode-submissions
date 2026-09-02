class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def validate(i, j, queens):
            for qi, qj in queens:
                if (
                    i == qi 
                    or j == qj
                    or abs(i - qi) == abs(j - qj)
                    
                ):
                    return False

            return True

        queens = set()
        res = []

        def backtrack(i, curr):

            if i == n:
                if len(queens) == n:
                    res.append(curr.copy())

                return

            for j in range(n):

                if validate(i, j, queens):
                    queens.add((i, j))
                    curr.append("." * j + "Q" + "." * (n - j - 1))

                    backtrack(i + 1, curr)

                    queens.remove((i, j))
                    curr.pop()

        backtrack(0, [])
        return res