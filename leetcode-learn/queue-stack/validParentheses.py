class Solution:
    def __init__(self):
        self.pairs = {"]": "[", "}": "{", ")": "("}

    def isValid(self, s: str) -> bool:
        stack = list()
        for bracket in s:
            if bracket in self.pairs.keys():
                if not stack or stack.pop() != self.pairs[bracket]:
                    # when stack is not empty, pop and check if matches.
                    # if stack is empty, close brackets cannot be appended. (+ "pop" method gets IndexError)
                    return False
            else:
                stack.append(bracket)

        if stack:
            # when stack is not empty. (there are brackets unmatched/not closed)
            return False
        return True


assert Solution().isValid("()[]{}") is True
assert Solution().isValid("(]") is False
assert Solution().isValid("]") is False
