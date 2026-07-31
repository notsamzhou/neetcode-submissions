class Solution:
    def check(self, nums: List[int]) -> bool:

        mid_found = 0

        i = 1
        while i < len(nums):
            if mid_found and (nums[i] > nums[0] or (mid_found != i and nums[i] < nums[i-1])):
                return False

            if not mid_found and nums[i] < nums[i-1]:
                mid_found = i

            i += 1

        return True
        