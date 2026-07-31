class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        best_k = max(piles)
        l, r = 1, max(piles)
        while l < r:

            mid = l + (r - l) // 2
            
            hours = 0
            for p in piles:
                hours += p // mid + bool(p % mid)

            if hours <= h:
                r = mid
                best_k = min(best_k, mid)

            if hours > h:
                l = mid + 1

        return best_k

            



        