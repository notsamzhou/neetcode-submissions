class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        used = set()
        res = []

        def backtrack(curr):

            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            position_used = set()
            for i in range(len(nums)):
                if i not in used and nums[i] not in position_used:
                    position_used.add(nums[i])
                    used.add(i)
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    used.remove(i)


        backtrack([])
        return res
