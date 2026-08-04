class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        columns = {i : set() for i in range(9)}
        rows = {i : set() for i in range(9)}
        boxes = {i : set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in columns[j]:
                        return False
                    columns[j].add(board[i][j])

                    if board[i][j] in rows[i]:
                        return False

                    rows[i].add(board[i][j])

                    box_id = j // 3 +  3 * (i // 3)

                    if board[i][j] in boxes[box_id]:
                        return False

                    boxes[box_id].add(board[i][j])

        return True
        