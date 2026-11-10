class Solution:
    def trap(self, height: List[int]) -> int:

        i, j = 0, len(height) - 1
        lMax, rMax = 0, 0

        res = 0
        while i <= j:
            if lMax < rMax:
                res += max(lMax - height[i], 0)
                lMax = max(height[i], lMax)
                i += 1

            else:
                res += max(rMax - height[j], 0)
                rMax = max(height[j], rMax)
                j -= 1

        return res


        