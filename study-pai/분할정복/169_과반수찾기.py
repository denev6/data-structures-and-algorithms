from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

class DivideAndConquerSolution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        left = self.majorityElement(nums[:mid])
        right = self.majorityElement(nums[mid:])

        return [left, right][nums.count(left) > mid]