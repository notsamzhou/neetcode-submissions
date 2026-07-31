class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m, n = len(matrix), len(matrix[0])


        top = 1
        for i in range(m):
            for j in range(n):

                if i == 0:
                    if matrix[i][j] == 0:
                        top = 0

                else:
                    if matrix[i][j] == 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = 0 if not matrix[i][0] or not matrix[0][j] else matrix[i][j]


        for i in range(1, m):
            matrix[i][0] =  0 if not matrix[i][0] or not matrix[0][0] else matrix[i][0]

        for j in range(n):
            matrix[0][j] =  0 if not matrix[0][j] or not top else matrix[0][j]

        
        