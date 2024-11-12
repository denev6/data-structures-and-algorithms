# IMPORTANT!!
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)


class Solution:
    """
    1. Get a list of accumulated product from the left.
    2. Use a pointer from the right to accumulate product of nums.
    """

    def productExceptSelf(self, nums):
        left_muls = []
        # left_muls[0]: 1
        # left_muls[1]: 1 * left_muls[0]
        # left_muls[2]: 1 * left_muls[0] * left_muls[1]
        # left_muls[n]: 1 * left_muls[0] * ... * left_muls[n-1]
        left_mul = 1
        for i in nums:
            left_muls.append(left_mul)
            left_mul = left_mul * i

        ans = [0 for _ in range(len(nums))]
        # To meet the problem condition(Follow up),
        # You can reuse "left_mul(list)" instead of creating a new list "ans".
        # In this code, I used a new list(ans) for better understanding.
        right_mul = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = right_mul * left_muls[i]
            right_mul = right_mul * nums[i]

        return ans
