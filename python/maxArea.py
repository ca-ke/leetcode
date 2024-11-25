import sys
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        firstPointer, secondPointer = 0, len(height) - 1
        maxArea = 0

        while firstPointer < len(height) and secondPointer >= 0:
            currentHeight = min(height[firstPointer], height[secondPointer])
            base = abs(firstPointer - secondPointer)
            currentArea = currentHeight * base
            maxArea = max(maxArea, currentArea)
            if height[firstPointer] < height[secondPointer]:
                firstPointer += 1
            else:
                secondPointer -= 1
        return maxArea


height = list(map(lambda x: int(x), sys.argv[1].split(",")))
print(Solution().maxArea(height))
