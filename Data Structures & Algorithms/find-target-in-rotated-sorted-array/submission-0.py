class Solution:
    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        # Find smallest number as the list's seperating point
        # Then do binary search on both lists O(2logn) = O(logn)
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        pivot = l
        if pivot == 0:
            # Array wasn't rotated at all
            return self.binary_search(nums, 0, len(nums)-1, target)
        elif nums[0] <= target <= nums[pivot-1]:
            return self.binary_search(nums, 0, pivot-1, target)
        else:
            return self.binary_search(nums, pivot, len(nums)-1, target)

        