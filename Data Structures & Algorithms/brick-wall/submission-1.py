class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        

        prefixSums = wall.copy()
        maximum = 0

        sumCounts = dict()

        for i in range(len(wall)):
            for j in range(len(wall[i]) - 1):
                if j != 0:
                    prefixSums[i][j] += prefixSums[i][j-1]

                if prefixSums[i][j] not in sumCounts:
                    sumCounts[prefixSums[i][j]] = 0

                sumCounts[prefixSums[i][j]] += 1

                if sumCounts[prefixSums[i][j]] > maximum:
                    maximum = sumCounts[prefixSums[i][j]]

        return len(wall) - maximum




