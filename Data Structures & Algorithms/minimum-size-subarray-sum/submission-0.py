class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        curr = 0
        res = math.inf
        for r in range(len(nums)):

            if curr < target:
                curr += nums[r]

            while l <= r and curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1


        return res if res != math.inf else 0
        