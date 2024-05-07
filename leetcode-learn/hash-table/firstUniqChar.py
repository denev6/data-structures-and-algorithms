class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict() # {char: (count, firstIndex)}
        for i, c in enumerate(s):
            if c not in count:
                count[c] = [0, i]
            count[c][0] += 1
 
        # As of Python 3.7, for the CPython implementation of Python, 
        # dictionaries remember the order of items inserted.
        for count, idx in count.values():
            if count == 1:
                return idx
        return -1