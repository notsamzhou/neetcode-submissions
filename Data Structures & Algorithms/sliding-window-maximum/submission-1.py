class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        res = []

        l, r = 0, 0
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()


            queue.append(i)
            r += 1
        
        res.append(nums[queue[0]])


        while r < len(nums):


            if l == queue[0]:
                queue.popleft()

            l += 1


            while queue and nums[r] >= nums[queue[-1]]:
                queue.pop()

            queue.append(r)
            res.append(nums[queue[0]])
            
            r += 1

        return res