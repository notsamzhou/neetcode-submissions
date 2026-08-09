class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        curr = (len(nums) + 0) * (len(nums) + 1) / 2
        for i in range(len(nums)):
            curr -= nums[i]

        return int(curr)
            


        