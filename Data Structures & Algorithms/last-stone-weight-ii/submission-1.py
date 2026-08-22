class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        target = sum(stones) // 2
        total = sum(stones)

        cache = {}
        def dp(i, curr_sum):
            if curr_sum >= target or i == len(stones):
                return abs(curr_sum - (total - curr_sum))


            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]

            res = min(dp(i + 1, curr_sum + stones[i]), dp(i + 1, curr_sum))

            cache[(i, curr_sum)] = res
            return res

        return dp(0, 0)
        