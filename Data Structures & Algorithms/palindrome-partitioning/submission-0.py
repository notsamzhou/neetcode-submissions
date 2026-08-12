class Solution:
    def partition(self, s: str) -> List[List[str]]:


        cache = {}
        def is_palindrome(i, j):

            if i > j or i < 0 or j >= len(s):
                return False

            if i == j:
                return True

            if (i, j) in cache:
                return cache[(i, j)]

            if (j - i) % 2:
                l = i + (j - i) // 2
                r = l + 1

                while i <= l and r <= j:
                    if s[l] != s[r]:
                        cache[(i, j)] = False
                        return False

                    l -= 1
                    r += 1

            else:
                mid = i + (j - i) // 2
                l = mid - 1
                r = mid + 1
                while i <= l and r <= j:
                    if s[l] != s[r]:
                        cache[(i, j)] = False
                        return False

                    l -= 1
                    r += 1

            cache[(i, j)] = True
            return True

        res = []
        curr = []

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    curr.append(s[i:j + 1])
                    backtrack(j + 1)
                    curr.pop()

        backtrack(0)
        return res
