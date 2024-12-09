class MySolution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0 for _ in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, _ = stack.pop()
                ans[idx] = i - idx
            stack.append((i, t))
        return ans


class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0 for _ in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                # when you need both index and value, 
                # save index and find values with list[index]
                # do not waste space and time
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i) # only index
        return ans


assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
