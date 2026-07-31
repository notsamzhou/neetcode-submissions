class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        counts = Counter(nums)
        for num in counts:
            if counts[num] % 2:
                return False

        return True
        