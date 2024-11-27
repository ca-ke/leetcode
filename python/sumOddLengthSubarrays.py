import sys
from typing import List


class Solution:
    def getArrayWithWindow(self, arr: List[int], k: int) -> int:
        result = 0
        windowSum = sum(arr[:k])
        result += windowSum

        for i in range(k, len(arr)):
            windowSum += arr[i] - arr[i - k]
            result += windowSum

        return result

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        totalSum = 0

        for i in range(1, len(arr) + 1, 2):
            totalSum += self.getArrayWithWindow(arr, k=i)
        return totalSum


arr = list(map(int, sys.argv[1].split(",")))
print(Solution().sumOddLengthSubarrays(arr))
