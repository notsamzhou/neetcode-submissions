class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixProd = [1 for i in range(len(nums))]
        suffixProd = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            prefixProd[i] = nums[i - 1] * prefixProd[i-1]


        for i in range(len(nums) - 2, -1, -1):
            suffixProd[i] = nums[i + 1] * suffixProd[i + 1]


        res = []
        for i in range(len(nums)):
            res.append(prefixProd[i] * suffixProd[i])

        return res
        