class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        curr = -math.inf

        for num in nums:
            curr = max(num, curr + num)
            res = max(curr, res)

        return res

        