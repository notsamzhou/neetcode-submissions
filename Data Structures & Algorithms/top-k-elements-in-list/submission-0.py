class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        heap = []
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))

        res = []
        for i in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)

        return res
        