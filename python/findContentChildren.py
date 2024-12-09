import sys
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        greedyPointer, sizePointer, count = 0, 0, 0

        while greedyPointer < len(g) and sizePointer < len(s):
            if g[greedyPointer] <= s[sizePointer]:
                count += 1
                greedyPointer += 1
            sizePointer += 1

        return count


g = list(map(int, sys.argv[1].split(",")))
s = list(map(int, sys.argv[2].split(",")))

print(Solution().findContentChildren(g, s))
