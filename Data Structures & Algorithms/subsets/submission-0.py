class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def helper(start, curr):

            res.append(curr.copy())

            for i in range(start, len(nums)):
                curr.append(nums[i])
                helper(i + 1, curr)
                curr.pop()

        helper(0, [])

        return res
        