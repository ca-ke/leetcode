import sys
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = (len(s) + len(spaces)) * [""]
        firstPointer = 0

        for i in range(len(result)):
            if firstPointer < len(spaces) and i - firstPointer == spaces[firstPointer]:
                result.append(" ")
                firstPointer += 1
            else:
                result.append(s[i - firstPointer])
        return "".join(result)


spaces = list(map(int, sys.argv[2].split(",")))
print(Solution().addSpaces(sys.argv[1], spaces))
