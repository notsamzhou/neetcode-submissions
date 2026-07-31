# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        
        def partition(pairs, l, r):
            pairs[r-1], pairs[l] = pairs[l], pairs[r-1]
            

            j = l
            for i in range(l+1, r):
                if pairs[i].key < pairs[l].key:
                    j += 1
                    pairs[i], pairs[j] = pairs[j], pairs[i]

            pairs[j], pairs[l] = pairs[l], pairs[j]

            return j

        def qsHelper(pairs, l, r):
            if r - l <= 1:
                return

            pivot_idx = partition(pairs, l, r)
            qsHelper(pairs, l, pivot_idx)
            qsHelper(pairs, pivot_idx + 1, r)

        qsHelper(pairs, 0, len(pairs))
        return pairs

        