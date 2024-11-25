import sys


class Solution:
    def isDivisor(self, str1: str, str2: str) -> bool:
        if len(str1) % len(str2) != 0:
            return False
        return str2 * (len(str1) // len(str2)) == str1

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        shorterString = str1 if len(str1) < len(str2) else str2

        for i in range(len(shorterString), 0, -1):
            candidate = shorterString[:i]
            if self.isDivisor(str1, candidate) and self.isDivisor(str2, candidate):
                return candidate

        return ""


print(Solution().gcdOfStrings(str1=sys.argv[1], str2=sys.argv[2]))
