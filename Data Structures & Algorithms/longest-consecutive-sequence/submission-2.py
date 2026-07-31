class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if num in seen:
                continue
            seen.add(num)

            left = mp[num - 1]
            right = mp[num + 1]
            length = left + right + 1

            mp[num - left] = length
            mp[num + right] = length

            res = max(res, length)

        return res