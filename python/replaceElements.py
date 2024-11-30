import sys
from typing import List


class Solution:
    def getMaxElement(self, arr: List[int], startPos: int) -> int:
        firstPointer, secondPointer = startPos, len(arr) - 1
        while firstPointer < secondPointer:
            if arr[firstPointer] < arr[secondPointer]:
                firstPointer += 1
            else:
                secondPointer -= 1
        return arr[firstPointer]

    def replaceElements(self, arr: List[int]) -> List[int]:
        maxValue = -999
        for i in range(len(arr) - 1):
            if maxValue <= arr[i]:
                maxValue = self.getMaxElement(arr, i + 1)
                arr[i] = maxValue
            else:
                arr[i] = maxValue
        arr[-1] = -1
        return arr


arr = list(map(int, sys.argv[1].split(",")))
print(Solution().replaceElements(arr))
