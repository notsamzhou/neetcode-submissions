class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        cache = {}
        def helper(curr):

            if curr == target:
                return 1

            if curr in cache:
                return cache[curr]

            res = 0
            for i in range( len(nums)):
                if curr + nums[i] <= target:
                    res += helper(curr + nums[i])

            cache[curr] = res
            return res


                


        return helper(0)
  
        