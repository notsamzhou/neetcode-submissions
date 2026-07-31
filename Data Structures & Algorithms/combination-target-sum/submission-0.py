class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        

        res = []

        def helper(start, current, comb):

            if current > target:
                return
            
            if current == target:
                res.append(comb.copy())

            for i in range(start, len(nums)):
                comb.append(nums[i])
                helper(i, current + nums[i], comb)
                comb.pop()

        helper(0, 0, [])

        return res
        