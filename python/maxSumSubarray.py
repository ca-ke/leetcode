import sys
from typing import List


class Solution:
    def maxSumSubarray(self, arr: List[int], k: int) -> int:
        firstPointer, secondPointer, count = 0, 0, 0
        maxCount = count

        while secondPointer < len(arr):
            if secondPointer - firstPointer + 1 > k:
                firstPointer += 1
                count -= arr[firstPointer - 1]
            count += arr[secondPointer]
            secondPointer += 1
            maxCount = max(maxCount, count)

        return maxCount


arr = list(map(int, sys.argv[1].split(",")))
k = int(sys.argv[2])
print(Solution().maxSumSubarray(arr, k))
