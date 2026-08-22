class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        counts = {5:0, 10:0, 20:0}

        for bill in bills:

            counts[bill] += 1

            if bill == 10:
                if not counts[5]:
                    return False

                counts[5] -= 1

            if bill == 20:
                if counts[10]:
                    counts[10] -= 1

                    if not counts[5]:
                        return False

                    counts[5] -= 1

                else:
                    counts[5] -= 3
                    if counts[5] < 0:
                        return False

            


    

        return True
                
        