class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def validate(i, j, columns, pos_diag, neg_diag):

            if j in columns or i + j in pos_diag or i - j in neg_diag:
                return False
            

            return True

        columns = set()
        pos_diag = set()
        neg_diag = set()
        res = []

        def backtrack(i, curr):

            if i == n:
                res.append(curr.copy())

                return

            for j in range(n):

                if validate(i, j, columns, pos_diag, neg_diag):

                    columns.add(j)
                    pos_diag.add(i + j)
                    neg_diag.add(i - j)
                    curr.append("." * j + "Q" + "." * (n - j - 1))

                    backtrack(i + 1, curr)

                    columns.remove(j)
                    pos_diag.remove(i + j)
                    neg_diag.remove(i - j)
                    curr.pop()

        backtrack(0, [])
        return res