class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = [(i, startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort(key=lambda x: (x[2], x[1]))

        cache = {}
        def dp(i):

            if i == 0:
                return jobs[0][3]

            if i in cache:
                return cache[i]
            start = jobs[i][1]
            priorJob = -1
            l = 0
            r = i - 1

            while l <= r:

                mid = (l + r) // 2
                if jobs[mid][2] <= start:
                    priorJob = max(priorJob, mid)
                    l = mid + 1

                else:
                    r = mid - 1

            res = max(jobs[i][3], dp(i - 1))
            if priorJob != -1 and priorJob != i:
                res = max(res, jobs[i][3] + dp(priorJob))

            cache[i] = res
            return cache[i]

        return dp(len(startTime) - 1)