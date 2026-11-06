class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0] * 10001
        for x in nums: points[x] += x
        prev = best = 0
        for score in points:
            prev, best = best, max(best, prev + score)
        return best
