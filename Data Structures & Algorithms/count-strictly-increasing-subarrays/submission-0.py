class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        cache = {}

        def dp(i):
            if i < 0:
                return 0

            res = 1

            if i > 0 and nums[i] > nums[i-1]:
                res += dp(i - 1)

            return res


        sums = [dp(i) for i in range(len(nums))]
        print(sums)
        return sum(sums)
        