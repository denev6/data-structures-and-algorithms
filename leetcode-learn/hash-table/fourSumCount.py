# O(N^2)

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        sum1 = collections.defaultdict(int)
        sum2 = collections.defaultdict(int)
        ans = 0

        for i in range(n):
            for j in range(n):
                sum1[nums1[i] + nums2[j]] += 1
                sum2[nums3[i] + nums4[j]] += 1
        
        for s1 in sum1.keys():
            if -s1 in sum2:
                ans += sum1[s1] * sum2[-s1]
        
        return ans
