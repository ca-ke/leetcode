import sys


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False

        firstPointer, secondPointer = 0, 0
        while secondPointer < len(s) and firstPointer < len(t):
            if t[firstPointer] == s[secondPointer]:
                firstPointer += 1
                secondPointer += 1
            else:
                firstPointer += 1
        return secondPointer == len(s)


s = sys.argv[1]
t = sys.argv[2]
print(Solution().isSubsequence(s, t))
