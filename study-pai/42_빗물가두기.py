# https://leetcode.com/problems/trapping-rain-water/description/


class Solution:
    """
    Imagine height: [2 0 1], then volumes: [0 1 0].
    So, we can assume that volume of certain point equals to
    'min(max height of left side, max height of right side) - current height'
    cuz two heights are trapping the water.
    So, the volume of the second point will be 1 = min(2, 1) - 0.

    We need to compute 'min(max height of left side, max height of right side)'
    and in this case only smaller value matters.

    So, use 'two pointer'.
    When the max-height of left side is larger, 
    then move the pointer of right side and vice versa
    cuz the larger value doesn't effect the result.
    All we care is the smaller one.
    """

    def trap(self, height) -> int:
        if not height:
            return 0

        volume = 0
        # set pointers left anf right
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            # Max height in the middle will never trap any water.
            # So, use < not <= .

            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


height = [4, 2, 0, 3, 2, 5]
assert Solution().trap(height) == 9
