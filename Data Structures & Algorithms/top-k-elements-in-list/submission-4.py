class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freqToNum = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            freqToNum[count].append(num)

        res = []
        for i in range(len(freqToNum) - 1, -1, -1):

            if len(freqToNum[i]) != 0:

                res.extend(freqToNum[i])

            if len(res) == k:
                return res

            