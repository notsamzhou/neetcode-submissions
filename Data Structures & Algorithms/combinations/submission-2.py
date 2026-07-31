class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def helper(i, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            if i > n:
                return

            comb.append(i)
            helper(i + 1, comb)
            comb.pop()
            helper(i + 1, comb)


        helper(1, [])
        return res
        