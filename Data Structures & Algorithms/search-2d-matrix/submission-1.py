class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        first, last = 0, len(matrix) - 1
        while first <= last:
            row = first + (last - first) // 2

            if target < matrix[row][0]:
                last = row - 1

            else:
                first = row + 1

        if last == len(matrix) or target > matrix[last][-1]:
            return False

        max_row = last

        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if target == matrix[max_row][mid]:
                return True

            if target < matrix[max_row][mid]:
                r = mid - 1

            else:
                l = mid + 1

        return False
        