class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        data = [(x ** 2 + y **2, (x, y)) for (x, y) in points]

        def partition(data, k, i, j):

            print(i)

            pivot = data[i][0]
            pivot_idx = i
            for l in range(i + 1, j + 1):
                if data[l][0] <= pivot:
                    pivot_idx += 1
                    data[l], data[pivot_idx] = data[pivot_idx], data[l]

            data[pivot_idx], data[i] = data[i], data[pivot_idx]

            if pivot_idx == k - 1:
                return data
            elif pivot_idx < k - 1:
                return partition(data, k, pivot_idx + 1, j)

            else:
                return partition(data, k, i, pivot_idx - 1)

        data = partition(data, k, 0, len(data) - 1)

        res = []
        for i in range(k):
            res.append(data[i][1])

        return res

                    

            
