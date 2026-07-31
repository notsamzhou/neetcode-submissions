class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}
        def helper(i, current):

            if i < 0:
                if current == 0:
                    return 1
                else:
                    return 0

            if (i, current) in cache:
                return cache[(i, current)]

            cache[(i, current)] = helper(i - 1, current + nums[i]) + helper(i - 1, current - nums[i])
            return cache[(i, current)]

            

            
        return helper(len(nums) - 1, target)

        