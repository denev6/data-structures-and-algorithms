# Can you come up with an algorithm that is less than O(n^2) time complexity?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_find = dict()
        # target == n1 + n2
        # target - n1 == n2
        # With n1, save (taget - n1) and find n2
        # If n2 in list -> return
        for i, n in enumerate(nums):
            if n in to_find.keys():
                return [to_find[n], i]
            to_find[target - n] = i