class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(i, current, comb):

            if current == target:
                res.append(comb.copy())
                return 
                
            if current > target:
                return

            if i >= len(candidates):
                return


            comb.append(candidates[i])
            helper(i + 1, current + candidates[i], comb)
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            helper(i + 1, current, comb)

        helper(0, 0, [])

        return res