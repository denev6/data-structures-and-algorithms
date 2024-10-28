class Solution:
    def evalRPN(self, tokens) -> int:
        expr = ["+", "-", "*", "/"]
        stack = list()
        for token in tokens:
            if token in expr:
                n2 = stack.pop()
                n1 = stack.pop()
                n = self.caculate(n1, n2, token)
                stack.append(n)
            else:
                stack.append(int(token))
        return stack[-1]

    def caculate(self, n1, n2, expr):
        match expr:
            case "+":
                return n1 + n2
            case "-":
                return n1 - n2
            case "*":
                return n1 * n2
            case "/":
                # The division between two integers always truncates toward zero.
                # i.e. 6 / -132 = 0
                return int(n1 / n2)


assert Solution().evalRPN(["4","13","5","/","+"]) == 6
assert Solution().evalRPN(["4","-2","/","2","-3","-","-"]) == -7
assert Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
