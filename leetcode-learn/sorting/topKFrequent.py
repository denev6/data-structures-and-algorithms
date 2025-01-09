from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        common = Counter(nums).most_common(k)
        return [c for c, _ in common]
        