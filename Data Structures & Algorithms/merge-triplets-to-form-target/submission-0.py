class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        

        found = [False, False, False]
        for triplet in triplets:

            for i in range(3):
                if triplet[i] == target[i]:
                    greater = False
                    for j in range(3):
                        if j != i:
                            if triplet[j] > target[j]:
                                greater = True

                    if not greater:
                        found[i] = True

        return found[0] and found[1] and found[2]
