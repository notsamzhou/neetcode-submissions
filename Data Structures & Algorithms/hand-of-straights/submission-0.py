from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False

        hashmap = defaultdict(int)
        for i in hand:
            hashmap[i] += 1


        for num in hand:
            start = num
            while hashmap[start - 1] > 0:
                start -= 1

            while start <= num:
                while hashmap[start] > 0:
                    for i in range(start, start + groupSize):
                        if hashmap[i] == 0:
                            return False

                        hashmap[i] -= 1

                start += 1


        return True

        


        