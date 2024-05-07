class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = list()
        for n in nums1:
            if n in nums2:
                ans.append(n)
                nums2.remove(n)
        return ans