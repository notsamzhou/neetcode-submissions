class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        offset = 0
        for i in range(len(nums)):

            if i >= 2 and nums[i] == nums[i - 2 - offset]:
                offset += 1

            else:
                nums[i - offset] = nums[i] 
        
        return len(nums) - offset