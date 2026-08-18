class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        processes = []
        for i, task in enumerate(tasks):
            processes.append((i, task[0], task[1]))

        #processes[i] = task Index, enqueueTime, processingTime

        processes.sort(key = lambda x: (x[1], x[2], x[0]))
        pq = [(processes[0][2], processes[0][0])]
        #pq = processingTime, task Index

        res = []
        i = 1
        curr_time = processes[0][1]
        while pq:

            processingTime, index = heapq.heappop(pq)
            res.append(index)
            curr_time += processingTime

            if not pq and i < len(processes):
                curr_time = max(curr_time, processes[i][1])
                heapq.heappush(pq, (processes[i][2], processes[i][0]))
                i += 1


            while i < len(processes) and processes[i][1] <= curr_time:

                heapq.heappush(pq, (processes[i][2], processes[i][0]))
                i += 1



            

        return res
