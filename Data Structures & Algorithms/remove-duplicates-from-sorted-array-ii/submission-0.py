class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        offset = 0
        curr = None
        count = 0
        for i in range(len(nums)):

            if nums[i] == curr:
                if count == 2:
                    offset += 1
                else:
                    nums[i - offset] = nums[i] 
                    count = 2
            else:
                if nums[i] != curr:
                    curr = nums[i]
                    count = 1

                nums[i - offset] = nums[i] 
        
        return len(nums) - offset