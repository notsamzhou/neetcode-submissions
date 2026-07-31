class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def helper(i, comb):

            if i > n:
                if len(comb) == k:
                    res.append(comb.copy())

                return

            comb.append(i)
            helper(i + 1, comb)
            comb.pop()
            helper(i + 1, comb)


        helper(1, [])
        return res
        