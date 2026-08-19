class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        prefixSum = [0] * len(nums)
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i - 1]

        res = math.inf

        for i in range(len(nums)):

            l = 0
            r = i

            while l <= r:
                mid = (l + r) // 2

                if nums[i] + prefixSum[i] - prefixSum[mid] >= target:
                    res = min(res, i - mid + 1)
                    l = mid + 1

                else:
                    r = mid - 1

        return res if res != math.inf else 0