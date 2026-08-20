class Solution:
    def maxCoins(self, nums: List[int]) -> int:


        cache  = {}

        def dp(l, r):
            if l > r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            res = 0
            for i in range(l, r + 1):
                popself = nums[i]
                if l > 0:
                    popself *= nums[l-1]
                if r < len(nums) - 1:
                    popself *= nums[r + 1]

                res = max(res, popself + dp(l, i - 1) + dp(i + 1, r))

            cache[(l, r)] = res
            return res

        return dp(0, len(nums) - 1)
