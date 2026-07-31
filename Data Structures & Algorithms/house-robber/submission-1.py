class Solution:
    def rob(self, nums: List[int]) -> int:

        from functools import lru_cache

        @lru_cache
        def dp(i):

            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[1], nums[0])

            return max(dp(i - 2) + nums[i], dp(i - 1))

        return dp(len(nums) - 1)

        