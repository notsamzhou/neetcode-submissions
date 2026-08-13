class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = Counter(nums)

        i = 0
        for num in [0, 1, 2]:
            for count in range(counts[num]):
                nums[i] = num
                i += 1
        