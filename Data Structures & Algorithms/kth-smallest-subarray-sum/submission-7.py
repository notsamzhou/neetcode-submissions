class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:

        def get_rank(x):
            left = 0
            total = 0
            result = 0

            for right in range(len(nums)):
                total += nums[right]

                while total > x:
                    total -= nums[left]
                    left += 1

                result += right - left + 1

            return result

        l = min(nums)
        r = sum(nums)
        res = l

        while l <= r:

            mid = (l + r) // 2
            rank = get_rank(mid)

            if rank < k:
                l = mid + 1

            else:
                r = mid - 1
                res = mid


        return res