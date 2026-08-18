class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1


        return j
        