# https://leetcode.com/problems/longest-palindromic-substring/description/


class MySolution:
    # 3559ms
    """
    Palindrome: 회문. 뒤집어도 같은 문자열
    >>> string == string[::-1]

    [[ Example ]]
    babad
    babad x
    baba x
     abad x
    bab o -> stop
    """

    def longestPalindrome(self, s: str) -> str:
        for len_word in range(len(s), 0, -1):
            for start in range(len(s) - len_word + 1):
                current = s[start : start + len_word]
                if self.is_palindrome(current):
                    return current

    def is_palindrome(self, s):
        return True if s == s[::-1] else False


class Solution:
    # 43ms
    """
    use sliding windows which have the length of 2 and 3.
    if the word filtered by window is palindrome,
    expand pointers left and right to check if there's longer palindrome.
    """

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        def expand(left, right):
            # expand pointers to find the longest palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            """Why 's[left+1:right]'?
            after the palindrome is found,
            there's additional 'left -= 1, right += 1' in while-loop.
            --> left: start of palindrome - 1
            --> right: end of palindrome + 1
            So, to return the palindrome, """
            return s[left + 1 : right]

        ans = ""
        for i in range(len(s) - 1):
            ans = max(
                ans,
                expand(i, i + 1),  # when the length of answer is even.
                expand(i, i + 2),  # when the length of answer is odd.
                key=len,
            )
        return ans


ans = Solution().longestPalindrome("babad")
assert ans == "bab" or ans == "aba"

ans = Solution().longestPalindrome("cbbd")
assert ans == "bb"

ans = Solution().longestPalindrome("a")
assert ans == "a"
