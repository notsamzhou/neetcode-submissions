class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr1, arr2):

            i = 0
            j = 0
            res = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1

            while i < len(arr1):
                res.append(arr1[i])
                i += 1

            while j < len(arr2):
                res.append(arr2[j])
                j += 1

            return res

        def mergeSort(i, j):

            if i >= j-1:
                return nums[i:j]
            mid = (i + j) // 2

            arr1 = mergeSort(i, mid)
            arr2 = mergeSort(mid, j)

            return merge(arr1, arr2)

        return mergeSort(0, len(nums))



        