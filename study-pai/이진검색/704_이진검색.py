# You must write an algorithm with O(log n) runtime complexity.


class MySolution:
    def search(self, nums, target) -> int:
        def binary_search(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)

        return binary_search(0, len(nums) - 1)


from bisect import bisect_left


class Solution:
    def search(self, nums, target) -> int:
        idx = bisect_left(nums, target)

        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1
