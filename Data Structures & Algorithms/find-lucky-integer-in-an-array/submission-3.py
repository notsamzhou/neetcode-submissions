class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1

        res = -1
        for num in counts:
            if counts[num] == num:
                res = max(res, num)

        return res