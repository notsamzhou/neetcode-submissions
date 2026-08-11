class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)

        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)

        time = 0

        queue = deque()
        while heap or queue:
            time += 1

            if heap:
                count = -heapq.heappop(heap)

                if count != 1:
                    queue.append((count - 1, time + n))

            if queue and queue[0][1] == time:

                heapq.heappush(heap, -queue.popleft()[0])

        return time
