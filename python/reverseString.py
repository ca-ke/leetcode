import sys
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        firstPointer, secondPointer = 0, len(s) - 1
        while firstPointer < secondPointer:
            s[firstPointer], s[secondPointer] = s[secondPointer], s[firstPointer]
            firstPointer += 1
            secondPointer -= 1


s = [char for char in sys.argv[1]]
Solution().reverseString(s)
print(s)
