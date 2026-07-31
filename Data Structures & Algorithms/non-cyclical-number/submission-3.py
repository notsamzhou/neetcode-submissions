class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(m):
            s = 0
            while m:
                s += (m % 10) ** 2
                m = m // 10

            return s

        slow = n
        fast = helper(n)
        while True:
            slow = helper(slow)
            fast = helper(helper(fast))

            if slow == fast:
                return fast == 1