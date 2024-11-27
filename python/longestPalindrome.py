import sys


class Solution:
    def expand(self, left: int, right: int, s: str) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            oddPalindrome = self.expand(i, i, s)
            evenPalindrome = self.expand(i, i + 1, s)
            result = max(result, oddPalindrome, evenPalindrome, key=len)
        return result


print(Solution().longestPalindrome(sys.argv[1]))
