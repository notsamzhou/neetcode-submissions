class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        cache = {}
        def dp(i, j, greater):
            
            if i == j:
                return True

            if (i, j, greater) in cache:
                return cache[(i, j, greater)]

            if greater:
                cache[(i, j, greater)] = arr[j] > arr[j - 1] and dp(i, j - 1, False)

            else:
                cache[(i, j, greater)] =  arr[j] < arr[j - 1] and dp(i, j - 1, True)

            return cache[(i, j, greater)]


        res = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):

                if dp(i, j, True) or dp(i, j, False):
                    res = max(res, j - i + 1)

        return res