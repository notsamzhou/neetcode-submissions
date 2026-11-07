class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:

        stack = []
        ans = [0] * len(nums)
        for right in range(len(nums) + 1):

            while stack and (right == len(nums) or nums[stack[-1]] >= nums[right]):
                idx = stack.pop()

                left = stack[-1] if stack else -1
                width = right - left - 1

                ans[width - 1] = max(ans[width - 1], nums[idx])

            stack.append(right)

        for width in range(len(nums) - 2, -1, -1):
            ans[width] = max(ans[width], ans[width+1])

        return ans