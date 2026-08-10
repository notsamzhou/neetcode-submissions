class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [-1]
        res = stack[0]

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                # stack[-1] is the shortest between i and stack[-2]
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                res = max(res, curr_height * curr_width)

            stack.append(i)

        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] - 1
            res = max(res, curr_height * curr_width)

        return res