class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        cache = {}
        def dp(i, M, player):
            if i >= len(piles):
                return 0

            if (i, M, player) in cache:
                return cache[(i, M, player)]

            if player:
                best = float("-inf")
                curr_sum = 0
                for x in range(2 * M):
                    if i + x < len(piles):
                        curr_sum += piles[i + x]
                        best = max(best, curr_sum + dp(i + x + 1, max(M, x + 1), False))

                cache[(i, M, player)] = best
                return cache[(i, M, player)]


            else:
                best = float("inf")

                for x in range(2 * M):
                    if i + x < len(piles):
                        best = min(best, dp(i + x + 1, max(M, x + 1), True))

                cache[(i, M, player)] = best

                return cache[(i, M, player)]


        return dp(0, 1, True)


