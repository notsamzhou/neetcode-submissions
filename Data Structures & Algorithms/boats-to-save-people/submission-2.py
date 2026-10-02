class Solution:

    
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        def testBoats(amt):
            
            used = 0
            i = 0
            j = len(people) - 1
            used = 0
            while i <= j:
                if people[i] + people[j] <= limit:

                    if used == amt:
                        return False

                    used += 1
                    i += 1
                    j -= 1

                else:
                    if used == amt:
                        return False
                    used += 1
                    j -= 1
            
            return True

        people.sort()

        maximum = max(people)

        if limit < maximum:
            return float('inf')

        l = len(people) // 2
        if len(people) % 2:
            l += 1
        r = len(people)

        res = r

        while l <= r:

            mid = (l + r) // 2

            fits = testBoats(mid)

            if fits:
                res = min(res, mid)
                r = mid - 1

            else:
                l = mid + 1

        return res

            

                

        