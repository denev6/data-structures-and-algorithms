class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0 for _ in range(len(temperatures))]
        # to caculate the distance between two value, record the index and use it as pointer.
        idx_stack = list()

        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            while idx_stack:
                # pop until there's lower temperature
                # and record the distance of index in "ans".
                if temperatures[idx_stack[-1]] >= current_temp:
                    break
                ans[idx_stack[-1]] = i - idx_stack[-1]
                idx_stack.pop()

            # push new temperature into stack
            idx_stack.append(i)

        return ans
        
assert Solution().dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert Solution().dailyTemperatures([30,40,50,60]) == [1,1,1,0]
