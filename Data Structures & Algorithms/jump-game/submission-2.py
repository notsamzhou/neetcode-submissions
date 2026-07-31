class Solution:
    def canJump(self, nums: List[int]) -> bool:

        queue = deque([0])
        visited = set()
        visited.add(0)

        while queue:

            j = queue.popleft()
            if j >= len(nums):
                continue
            if j == len(nums) - 1:
                return True

            for i in range(nums[j] + 1):
                if i + j not in visited:
                    visited.add(i + j)
                    queue.append(i + j)


        

        return False
        