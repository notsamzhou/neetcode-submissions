class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        from functools import lru_cache

        @lru_cache()
        def dp(cur_step):

            if cur_step == 0 or cur_step == 1:
                return 0

            return min(dp(cur_step - 1) + cost[cur_step - 1], dp(cur_step-2) + cost[cur_step-2])

        return dp(len(cost))