class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        pos_char = dict()
        for end, c in enumerate(s):
            if c in pos_char:
                start = max(start, pos_char[c] + 1)
            pos_char[c] = end
            max_len = max(max_len, end - start + 1)
        return max_len