from typing import List
import sys


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]
        for i, num in enumerate(gain):
            result.insert(i + 1, result[i] + num)

        result.sort()
        return result[-1]


gain = list(map(int, sys.argv[1].split(",")))
print(Solution().largestAltitude(gain))
