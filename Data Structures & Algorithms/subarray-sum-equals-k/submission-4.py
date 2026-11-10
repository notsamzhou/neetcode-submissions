class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        freq = dict()
        freq[0] = 1

        res = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in freq:
                res += freq[s - k]

            freq[s]  = freq.get(s, 0) + 1

            
        return res