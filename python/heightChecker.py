import sys
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = [value for value in heights]
        expected.sort()
        result = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1

        return result


heights = list(map(int, sys.argv[1].split(",")))
print(Solution().heightChecker(heights))
