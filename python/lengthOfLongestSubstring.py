import sys


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChar = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in seenChar:
                seenChar.remove(s[left])
                left += 1
            seenChar.add(s[right])
            result = max(result, right - left + 1)
        return result


print(Solution().lengthOfLongestSubstring(sys.argv[1]))
