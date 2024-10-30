# https://leetcode.com/problems/two-sum/description/


class MySolution:
    # 1734ms
    """O(N^2) Brute-force"""

    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    # 2ms
    """Main idea
    instead of check 'i + j == target',
    check if j(target - i) is in nums.
    + use hash-map to search faster.
    """

    def twoSum(self, nums, target):
        # turn nums(list) to hash-map
        nums_map = dict()
        for i, n in enumerate(nums):
            nums_map[n] = i

        # search
        for i, n in enumerate(nums):
            to_search = target - n
            if to_search in nums_map and i != nums_map[to_search]:
                return [i, nums_map[to_search]]


nums = [2, 7, 11, 15]
target = 9
assert Solution().twoSum(nums, target) == [0, 1]

nums = [3, 2, 4]
target = 6
assert Solution().twoSum(nums, target) == [1, 2]
