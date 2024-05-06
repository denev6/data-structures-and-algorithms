class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while True:
            squared = sum(int(i) ** 2 for i in str(n))
            if squared == 1:
                return True
            elif squared in history:
                return False
            history.add(squared)
            n = squared