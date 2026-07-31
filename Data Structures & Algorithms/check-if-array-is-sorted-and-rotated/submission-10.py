class Solution:
    def check(self, nums: List[int]) -> bool:

        inversion_found = False
        n = len(nums)

        for i in range(n):
            if nums[i] < nums[(i - 1) % n]:
                if inversion_found:
                    return False
                inversion_found = True
                
        
        return True