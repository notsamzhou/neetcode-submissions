class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqToNums = [[] for i in range(len(nums) + 1)]

        for key, val in counts.items():
            freqToNums[val].append(key)

        res = []
        for i in range(len(freqToNums) - 1, -1 , -1):
            res.extend(freqToNums[i])
            if len(res) >= k:
                break

        return res

        