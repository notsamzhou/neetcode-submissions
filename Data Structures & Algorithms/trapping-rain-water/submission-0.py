class Solution:
    def trap(self, height: List[int]) -> int:
        

        prefix_height = [0] * len(height)
        suffix_height = [0] * len(height)

        for i in range(1, len(height)):
            prefix_height[i] = max(prefix_height[i - 1], height[i - 1])



        for i in range(len(height) - 2, -1, -1):
            suffix_height[i] = max(suffix_height[i + 1], height[i + 1])

        res = 0
        for i in range(len(height)):

            limit = min(prefix_height[i], suffix_height[i])

            res += max(0, limit - height[i])

        return res
