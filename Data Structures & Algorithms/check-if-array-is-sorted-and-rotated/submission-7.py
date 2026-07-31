class Solution:
    def check(self, nums: List[int]) -> bool:

        mid_found = False
        minimum = nums[0]

        i = 1
        while i < len(nums):
            if mid_found and nums[i] > nums[0]:
                return False

            if not mid_found and nums[i] < nums[i-1]:
                mid_found = True

            i += 1

        return True
        