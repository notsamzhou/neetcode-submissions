class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs_helper(i, capacity):
            if i == len(profit):
                return 0

            if (i, capacity) in cache:
                return cache[(i, capacity)]

            cache[(i, capacity)] = dfs_helper(i + 1, capacity)

            new_cap = capacity - weight[i]
            if new_cap >= 0:
                cache[(i, capacity)] = max(cache[(i, capacity)], profit[i] + dfs_helper(i, new_cap))

            return cache[(i, capacity)]

        cache = {}

        return dfs_helper(0, capacity)

