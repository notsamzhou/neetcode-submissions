class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        values = sorted(list(set(nums)))


        prev2, prev1 = 0, 0
        for i in range(len(values)):
            val = values[i]

            fromVal = counts[val] * val

            if i > 0 and values[i] == values[i-1] + 1:
                temp = prev1
                prev1 = max(prev1, fromVal + prev2)
                prev2 = temp
            else:
                prev2 = prev1
                prev1 = fromVal + prev1

        return prev1
                
