class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        summedIdx = {s:i for i, s in enumerate(list1)}
        summedStr = set() # strings that exist in both list
        for i, s in enumerate(list2):
            if s in summedIdx:
                summedIdx[s] += i
                summedStr.add(s)

        # find min-sum strings
        ans = list()
        minSum = float('inf')
        for s in summedStr:
            summed = summedIdx[s]
            if summed < minSum:
                minSum = summed
                ans.clear()
                ans.append(s)
            elif summed == minSum:
                ans.append(s)
        return ans