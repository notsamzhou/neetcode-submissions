class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        return max(self._rob_range(nums[:-1]), self._rob_range(nums[1:]))

    def _rob_range(self, nums):
        prev2, prev1 = 0, 0

        for num in nums:
            temp = max(num + prev2, prev1)

            prev1, prev2 = temp, prev1

        return prev1
        