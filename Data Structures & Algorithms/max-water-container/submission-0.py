class Solution:
    def maxArea(self, heights: List[int]) -> int:

        def area(i, j):
            return min(heights[i], heights[j]) * (j - i)

        start = 0
        end = len(heights) - 1

        res = area(start, end)
        while start < end:

            res = max(res, area(start, end))
            if heights[start] < heights[end]:
                start += 1

            else:
                end -= 1

        return res

        