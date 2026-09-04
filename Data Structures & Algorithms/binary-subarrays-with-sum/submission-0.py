class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSums = defaultdict(int)
        prefixSums[0] = 1


        res = 0
        currSum = 0
        for num in nums:
            currSum += num

            

            res += prefixSums[currSum - goal]

            prefixSums[currSum] += 1

        return res