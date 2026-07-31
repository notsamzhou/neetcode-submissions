class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)

        dp1 = [0] * (n - 1) # [0, n - 2]
        dp1[0] = nums[0]

        dp2 = [0] * (n - 1) # [1, n - 1]
        dp2[0] = nums[1]


        for i in range(1, n - 1):
            rob = dp1[i-2] + nums[i] if i > 1 else nums[i]
            dp1[i] = max(dp1[i - 1], rob)

        for i in range(1, n - 1):
            rob = dp2[i-2] + nums[i+1] if i > 1 else nums[i+1]
            dp2[i] = max(dp2[i - 1], rob)

        return max(dp1[n - 2], dp2[n-2])
        