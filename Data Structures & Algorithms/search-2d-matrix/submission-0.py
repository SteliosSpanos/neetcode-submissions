class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [num for row in matrix for num in row]
        # The array is sorted
        l, r = 0, len(flat) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        