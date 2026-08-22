class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:


        projects = [(capital[i], profits[i]) for i in range(len(profits))]

        projects.sort()
        i = 0

        heap = []

        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(heap, (-projects[i][1]))
            i += 1

        
        jobs = 0
        while jobs < k and heap:

            profit = -heapq.heappop(heap)
            jobs += 1
            w += profit

            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, (-projects[i][1]))
                i += 1

        return w


            