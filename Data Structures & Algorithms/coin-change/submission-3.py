class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = [[-1] * (amount + 1) for _ in range(len(coins))]
        def dp(coin, amt):

            if amt == 0:
                return 0

            if coin < 0:
                return math.inf

            if amt < 0:
                return math.inf   
            
            if cache[coin][amt] != -1:
                return cache[coin][amt]

            best = dp(coin-1, amt)
            count = 1
            while amt - coins[coin] * count >= 0:
                best = min(best, count + dp(coin-1, amt - count * coins[coin]))
                count += 1

            cache[coin][amt] = best

            return cache[coin][amt]

        res = dp(len(coins) - 1, amount)

        return res if res != math.inf else -1
        