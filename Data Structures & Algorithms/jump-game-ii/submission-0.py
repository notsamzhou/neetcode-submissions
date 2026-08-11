class Solution:
    def jump(self, nums: List[int]) -> int:

        cache = {}
        def dp(i):

            if i >= len(nums) - 1:
                return 0

            if i in cache:
                return cache[i]

            res = float('inf')
            for j in range(i + 1, i + nums[i] + 1):
                res = min(res, 1 + dp(j))

            cache[i] = res
            return cache[i]

        return dp(0)
