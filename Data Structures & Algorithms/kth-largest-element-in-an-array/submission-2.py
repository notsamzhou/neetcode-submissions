class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        


        k= len(nums) - k + 1
        def partition(arr):

            pivot = arr[0]
            i = 0

            for j in range(1, len(arr)):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[0], arr[i] = arr[i], arr[0]

            return i

        def quickselect(arr, target):
            pivot_idx = partition(arr)

            if target == pivot_idx + 1:
                return arr[pivot_idx]

            if target < pivot_idx + 1:
                return quickselect(arr[:pivot_idx], target)

            else:
                return quickselect(arr[pivot_idx + 1:], target - (pivot_idx + 1))

        return quickselect(nums, k)