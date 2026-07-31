class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        present = set()
        for num in nums:
            present.add(num)

        res = 0

        for num in nums:
            if num - 1 in present:
                continue

            curr = num
            cnt = 1
            while curr + 1 in present:
                curr +=1
                cnt += 1

            res = max(res, cnt)
            
        
        return res
        