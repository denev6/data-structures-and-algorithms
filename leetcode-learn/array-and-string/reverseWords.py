# Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        s = s[::-1]
        return " ".join(s)