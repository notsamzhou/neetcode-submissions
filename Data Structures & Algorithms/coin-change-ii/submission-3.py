class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = [[None] * (amount + 1) for _ in range(len(coins))]
        def dp(c, amt):

            if amt == 0:
                return 1

            if c < 0 or amt < 0:
                return 0

            if cache[c][amt] is not None:
                return cache[c][amt]

            cache[c][amt] = dp(c, amt - coins[c]) + dp(c - 1, amt)

            return cache[c][amt]

        return dp(len(coins)-1, amount)