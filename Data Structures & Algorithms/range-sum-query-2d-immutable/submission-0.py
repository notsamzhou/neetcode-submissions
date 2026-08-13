class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.sum_total = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                left = self.sum_total[i][j - 1] if j > 0 else 0
                up = self.sum_total[i - 1][j] if i > 0 else 0
                corner = self.sum_total[i - 1][j-1] if i > 0 and j > 0 else 0
                self.sum_total[i][j] = matrix[i][j] + left + up - corner
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = self.sum_total[row2][col2]
        up = self.sum_total[row1 - 1][col2] if row1 > 0 else 0
        left = self.sum_total[row2][col1 - 1] if col1 > 0 else 0
        corner = self.sum_total[row1 - 1][col1 -1] if row1 > 0 and col1 > 0 else 0

        return total - up - left + corner

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)