class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        n = len(nums)

        prefixSums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefixSums[i] = prefixSums[i-1] + nums[i-1]

        
        cache = {}
        def dp(i, k_left):
            if i < 0 and k_left != 0:
                return math.inf

            if i < 0 and k_left == 0:
                return -math.inf

            if k_left == 1:
                return prefixSums[i + 1]

            if (i, k_left) in cache:
                return cache[(i, k_left)]

            res = math.inf
            for j in range(k_left-1, i + 1):

                res = min(res, max(prefixSums[i+1]- prefixSums[j], dp(j - 1, k_left - 1)))

            

            cache[(i, k_left)] = res
            return cache[(i, k_left)]

        return dp(n - 1, k)


        

        