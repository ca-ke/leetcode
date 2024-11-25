import sys


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        firstPointer, secondPointer = 0, len(s) - 1
        while firstPointer < secondPointer:
            if s[firstPointer] == s[secondPointer]:
                firstPointer += 1
                secondPointer -= 1
            else:
                return False

        return True


print(Solution().isPalindrome(sys.argv[1]))
