class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)
        print(total)
        if total % k:
            return False

        goal = total // k

        mask = 0
        cache = {}
        def dp(mask, target, sets):

            if sets == k:
                return True

            if target == 0:
                return dp(mask, goal, sets + 1)

            if target < 0:
                return False

            if mask in cache:
                return cache[mask]

            for i in range(len(nums)):
                if not mask & (1 << i):

                    if dp(mask | (1 << i), target - nums[i], sets):
                        cache[mask] = True
                        return True

            cache[mask] = False
            return False

        return dp(mask, goal, 0)
        