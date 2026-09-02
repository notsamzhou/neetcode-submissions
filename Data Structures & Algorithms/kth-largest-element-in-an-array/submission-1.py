class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        


        target = len(nums) - k + 1
        def partition(arr, l, r):



            pivot = arr[l]
            i = l

            for j in range(l + 1, r):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[l], arr[i] = arr[i], arr[l]

            return i

        def quickselect(arr, l, r):
            pivot_idx = partition(arr, l, r)

            if target == pivot_idx + 1:
                return nums[pivot_idx]

            if target < pivot_idx + 1:
                return quickselect(arr, l, pivot_idx)

            else:
                return quickselect(arr, pivot_idx + 1, r)

        return quickselect(nums, 0, len(nums))