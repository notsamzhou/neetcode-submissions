class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs_helper(cap):

            if cap in cache:
                return cache[cap]

            curr_max = 0

            for i in range(len(profit)):
                new_cap = cap - weight[i]
                if new_cap >= 0:
                    curr_max = max(curr_max, profit[i] + dfs_helper(new_cap))
                    

            cache[cap] = curr_max
                    
            return cache[cap] 



        cache = {}

        return dfs_helper(capacity)

