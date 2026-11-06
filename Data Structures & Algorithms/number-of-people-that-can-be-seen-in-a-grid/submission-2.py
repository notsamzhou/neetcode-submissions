class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])

        ans = [[0] * N for _ in range(M)]

        for i in range(M):

            stack = [heights[i][N-1]]
            ans[i][N-1] = 0

            for j in range(N - 2, -1, -1):

                while stack and stack[-1] < heights[i][j]:
                    ans[i][j] += 1
                    stack.pop()

                if stack:
                    ans[i][j] += 1

                    if stack[-1] == heights[i][j]:
                        stack.pop()

                stack.append(heights[i][j])

        for j in range(N):

            stack = [heights[M - 1][j]]

            for i in range(M - 2, -1, -1):

                while stack and stack[-1] < heights[i][j]:
                    ans[i][j] += 1
                    stack.pop()

                if stack:
                    ans[i][j] += 1

                    if stack[-1] == heights[i][j]:
                        stack.pop()

                stack.append(heights[i][j])


        return ans
