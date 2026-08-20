class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixSumCounts = defaultdict(int)

        res = 0
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            print(prefixSum)

            if prefixSum == k:
                res += 1

            

            res += prefixSumCounts[prefixSum - k]
            prefixSumCounts[prefixSum] += 1

            

        return res
            

        