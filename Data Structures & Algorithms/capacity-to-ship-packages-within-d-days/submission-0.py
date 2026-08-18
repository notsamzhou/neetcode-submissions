class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)

        res = sum(weights)

        while l <= r:
            cap = (l + r) // 2

            days_taken = 1
            curr = 0
            for weight in weights:
                if curr + weight > cap:
                    days_taken += 1
                    curr = weight

                else:
                    curr += weight


            if days_taken <= days:
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res
        