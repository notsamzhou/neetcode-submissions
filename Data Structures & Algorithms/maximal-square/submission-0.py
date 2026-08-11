class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                dp[i][j] = int(matrix[i][j])
                if j > 0 and dp[i][j] == 1:
                    dp[i][j] += dp[i][j-1]


        for j in range(len(matrix[0])):


            i = 0

            queue = deque()
            while i < len(matrix):

                candidate = dp[i][j]
                
                while queue and dp[queue[0]][j] > candidate:
                    front = queue.popleft()

                if candidate != 0:
                    queue.append(i)

                while queue and i - queue[0] + 1 == dp[queue[0]][j]:
                    
                    res = max(res, dp[queue.popleft()][j] ** 2)

                i += 1



        return res
                
