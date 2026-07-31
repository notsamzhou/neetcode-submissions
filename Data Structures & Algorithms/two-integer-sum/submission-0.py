class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        targets = dict()

        for i in range(len(nums)):
            if target - nums[i] in targets.keys():
                return [targets[target - nums[i]], i]

            targets[nums[i]] = i

        

        