class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums) # k can be very large

        start = 0
        count = 0

        while count < len(nums):

            nxt = (start + k) % len(nums)
            curr = nums[start]

            while nxt != start:
                temp = nums[nxt]
                nums[nxt] = curr
                curr = temp

                nxt = (nxt + k) % len(nums)


                count += 1

            nums[nxt] = curr
            count += 1

            if count < len(nums):
                start += 1





        