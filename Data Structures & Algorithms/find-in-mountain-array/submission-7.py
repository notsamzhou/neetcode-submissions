class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        #find inversion point
        l = 1
        r = mountainArr.length() - 2

        while l < r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)

            if mid_val < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid

        apex = l
        apex_val = mountainArr.get(apex)
        if apex_val == target:
            return apex

        l, r = 0, apex
        print(apex)

        while l < r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)

            if mid_val < target:
                l = mid + 1
            elif mid_val > target:
                r = mid - 1

            elif mid_val == target:
                return mid

        if mountainArr.get(l) == target:
            return l

        l, r = apex + 1, mountainArr.length() - 1
        

        print("second half")

        while l < r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)

            if mid_val > target:
                l = mid + 1
            elif mid_val < target:
                r = mid - 1

            elif mid_val == target:
                return mid

        if mountainArr.get(l) == target:
            return l

        return -1

        