class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        # dp[i] = longest ending at i
        cache = {}
        def dp(i, greater):
            
            if i == 0:
                return 1

            if (i, greater) in cache:
                return cache[(i, greater)]

            if greater:
                if arr[i] > arr[i - 1]:
                    cache[(i,greater)] = 1 + dp(i - 1, False)

                else:
                    cache[(i, greater)] = 1


            else:
                if arr[i] < arr[i - 1]:
                    cache[(i, greater)] =  1 + dp(i - 1, True)

                else:
                    cache[(i, greater)] = 1

            return cache[(i, greater)]


        res = 0
        for i in range(len(arr)):
            res = max(res, dp(i, True), dp(i, False))

        return res