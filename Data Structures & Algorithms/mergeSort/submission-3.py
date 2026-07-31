# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, l, m, r):
        arr1 = pairs[l:m + 1]
        arr2 = pairs[m + 1:r]

        i = 0
        j = 0
        k = l

        while i < len(arr1) and j < len(arr2):
            if arr1[i].key <= arr2[j].key:
                pairs[k] = arr1[i]
                i += 1
            else:
                pairs[k] = arr2[j]
                j += 1
            k += 1

        while i < len(arr1):
            pairs[k] = arr1[i]
            i += 1
            k += 1
        while j < len(arr2):
            pairs[k] = arr2[j]
            j += 1
            k += 1

    def mergeHelper(self, pairs, l, r):
        if r - l <= 1:
            return

        m = l + (r - 1- l) // 2
        self.mergeHelper(pairs, l, m + 1)
        self.mergeHelper(pairs, m + 1, r)
        self.merge(pairs, l, m, r)
        


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeHelper(pairs, 0, len(pairs))
        return pairs

        


