import sys


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = []
        for word in s.split(" "):
            if word != "":
                result.append(word)
        return len(result[-1])


print(Solution().lengthOfLastWord(sys.argv[1]))
