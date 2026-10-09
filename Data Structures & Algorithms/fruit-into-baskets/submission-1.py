class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        counts = dict()
        used = 0
        res = 0

        l = 0
        for r in range(len(fruits)):

            if fruits[r] not in counts:
                counts[fruits[r]] = 0
            
            if counts[fruits[r]] == 0:
                used += 1

            counts[fruits[r]] += 1
            

            while used > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    used -= 1

                l += 1

            res = max(res, r - l + 1)

        return res

            
        