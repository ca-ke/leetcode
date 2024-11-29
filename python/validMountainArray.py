import sys
from typing import List


class Solution:
    def isDecreasing(self, arr: List[int], start: int) -> bool:
        for i in range(start, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True

    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        i = 0
        n = len(arr)

        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        return self.isDecreasing(arr, i)


arr = list(map(int, sys.argv[1].split(",")))
print(Solution().validMountainArray(arr))
