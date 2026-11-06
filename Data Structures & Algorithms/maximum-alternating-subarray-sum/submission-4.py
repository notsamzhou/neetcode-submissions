class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        odd = even = answer = -10**18
        for value in nums:
            odd, even = max(value, even + value), odd - value
            answer = max(answer, odd, even)
        return answer