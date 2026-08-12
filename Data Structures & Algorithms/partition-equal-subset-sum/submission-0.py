class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        goal = total // 2
        cache = {}

        def dp(i, target):
            if i < 0:
                if target != 0:
                    return False

                return True
            
            if (i, target) in cache:
                return cache[(i, target)]

            cache[(i, target)] = dp(i - 1, target) or dp(i - 1, target - nums[i])
            return cache[(i, target)]

        return dp(len(nums) - 1, goal)
        