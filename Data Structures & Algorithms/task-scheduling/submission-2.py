class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        processing_q = deque()
        counts = Counter(tasks)
        heap = []
        for task, count in counts.items():
            heapq.heappush_max(heap, (count, task))

        time = 0

        while heap or processing_q:
            if not heap:
                end_time, count, task = processing_q.popleft()
                heapq.heappush_max(heap, (count, task))
                time = end_time

            if processing_q and processing_q[0][0] <= time:
                _, count, task = processing_q.popleft()
                heapq.heappush_max(heap, (count, task))

            count, task = heapq.heappop_max(heap)
            if count > 1:
                processing_q.append((time + n + 1, count - 1, task))

            time += 1

        return time
