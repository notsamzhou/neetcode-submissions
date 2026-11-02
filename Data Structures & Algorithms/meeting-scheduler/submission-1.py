class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])

        i, j = 0, 0

        while i < len(slots1) and j < len(slots2):
            max_start = max(slots1[i][0], slots2[j][0])
            min_end = min(slots1[i][1], slots2[j][1])

            if min_end - max_start >= duration:
                return [max_start, max_start + duration]


            if slots1[i][1] < slots2[j][1]:
                i += 1

            else:
                j += 1

        return []


        