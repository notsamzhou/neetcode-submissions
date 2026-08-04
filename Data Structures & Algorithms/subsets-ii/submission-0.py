class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        def helper(start, curr):
            res.append(curr.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                helper(i + 1, curr)
                curr.pop()

        helper(0, [])
        return res
            
        