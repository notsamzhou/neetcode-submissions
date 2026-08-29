class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = [[-1] * (amount + 1) for _ in range(len(coins))]
        def dp(coin, amt):

            if coin < 0:
                return math.inf

            if amt < 0:
                return math.inf

            if amt == 0:
                return 0
            
            if cache[coin][amt] != -1:
                return cache[coin][amt]

            use = 1 + dp(coin, amt - coins[coin])
            skip = dp(coin - 1, amt)

            cache[coin][amt] = min(use, skip)

            return cache[coin][amt]

        res = dp(len(coins) - 1, amount)

        return res if res != math.inf else -1
        