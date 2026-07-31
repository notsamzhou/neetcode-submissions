class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                break

            if i == len(nums) - 1:
                return True

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                break

            if i == len(nums) - 1:
                return True

        return False
        