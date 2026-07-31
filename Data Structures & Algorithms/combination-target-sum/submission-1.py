class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

                

        res = []

        def helper(i, current, comb):

            if current == target:
                res.append(comb.copy())
                return

            if current > target:
                return

            if i >= len(nums):
                return

                
            

            comb.append(nums[i])
            helper(i, current + nums[i], comb)
            comb.pop()
            helper(i + 1, current, comb)

        helper(0, 0, [])

        return res
        
        