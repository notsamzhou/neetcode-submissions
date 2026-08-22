class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        dp = nums.copy()

        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i-1] + nums[i])

        minSuffix = [math.inf] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            minSuffix[i] = min(nums[i + 1], nums[i + 1]+ minSuffix[i + 1])



        res = -math.inf
        total = sum(nums)
        for i in range(len(nums)):
            res = max(res, dp[i], total - minSuffix[i])

        return res