class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums.sort()
        max_diff = 0
        
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff > max_diff:
                max_diff = diff
        return max_diff
