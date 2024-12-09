from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        seen = set()
        stack = []

        for char in s:
            counter[char] -= 1
            if char in seen:
                # skip if char is already seen.
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                # if (char exists in the stack)
                # and (char is lexicographically smaller than the last char in the stack)
                # and (there is a same char not being seen yet.)

                # then remove the one added in the stack(answer)
                # to append a new one later.
                # it helps making a lexicographically smaller answer.
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return "".join(stack)


assert Solution().removeDuplicateLetters("bcabc") == "abc"
assert Solution().removeDuplicateLetters("cbacdcbc") == "acdb"
assert Solution().removeDuplicateLetters("ecabc") == "eabc"
