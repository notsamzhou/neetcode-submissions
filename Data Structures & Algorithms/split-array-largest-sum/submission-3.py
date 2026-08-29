class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        n = len(nums)

        prefixSums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefixSums[i] = prefixSums[i-1] + nums[i-1]

        def checkMaxSum(maximum):
            k_left = k

            i = 0
            for j in range(n):

                if prefixSums[j + 1] - prefixSums[i] > maximum:
                    if j == i:
                        return False

                    i = j
                    k_left -= 1

            return k_left >= 1


        l, r = max(nums), sum(nums)
        res = sum(nums)

        while l <= r:

            mid = l  + (r - l) // 2

            passed = checkMaxSum(mid)

            if passed:
                r = mid-1
                res = mid

            else:
                l = mid + 1
        return res


        