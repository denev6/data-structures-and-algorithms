import heapq

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heapq.heapify(nums) # min heap

        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)