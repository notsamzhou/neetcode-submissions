class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freqToNum = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            freqToNum[count].append(num)

        res = []
        for i in range(len(freqToNum) - 1, -1, -1):

            while len(freqToNum[i]) > 0:
                res.append(freqToNum[i].pop())

            if len(res) == k:
                return res

            