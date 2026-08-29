class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l = 0
        r = len(nums)-1

        while l <= r:

            if nums[l] <= nums[r]:
                for j in range(l, r + 1):
                    if nums[j] == target:
                        return True

                return False


            mid = l + (r - l) // 2

            if nums[mid] == target:
                True

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid

                else:
                    l = mid + 1

            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid

                else:
                    r = mid - 1

        return False

            