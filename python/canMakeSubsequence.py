import sys


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        firstPointer, secondPointer = 0, 0

        while firstPointer < len(str1) and secondPointer < len(str2):
            if (
                str1[firstPointer] == str2[secondPointer]
                or (str1[firstPointer] == "z" and str2[secondPointer] == "a")
                or (chr(ord(str1[firstPointer]) + 1) == str2[secondPointer])
            ):
                secondPointer += 1
            firstPointer += 1

        return secondPointer == len(str2)


print(Solution().canMakeSubsequence(sys.argv[1], sys.argv[2]))
