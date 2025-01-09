class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idxNums = dict()
        for i, n in enumerate(nums):
            if (n in idxNums and i - idxNums[n] <= k):
                return True
            idxNums[n] = i
        return False