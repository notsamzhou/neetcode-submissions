class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1

                elif nums[val-1] == 0:
                    nums[val - 1] = -val


        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        
        return len(nums) + 1
        