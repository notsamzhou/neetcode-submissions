class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        used = set()
        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())

            for num in nums:
                if num not in used:
                    used.add(num)
                    curr.append(num)
                    helper(curr)
                    curr.pop()
                    used.remove(num)
        helper([])
        return res
        