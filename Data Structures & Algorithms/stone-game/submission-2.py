class Solution:
    def stoneGame(self, piles: List[int]) -> bool:


        
        cache = {}

        def dp(i, j):

            if (i, j) in cache:
                return cache[(i, j)]
            if i == j:
                cache[(i, j)] = -piles[i]
                return cache[(i, j)]

            if not (j - i) % 2:
                cache[(i, j)] = min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

            else:
                cache[(i, j)] = max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))

            return cache[(i, j)]


        return dp(0, len(piles) - 1) > 0