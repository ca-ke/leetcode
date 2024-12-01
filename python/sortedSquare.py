import sys
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        firstPointer, secondPointer, resultPointer = 0, len(nums) - 1, len(nums) - 1

        while firstPointer <= secondPointer:
            if abs(nums[firstPointer]) > abs(nums[secondPointer]):
                result[resultPointer] = nums[firstPointer] * nums[firstPointer]
                firstPointer += 1
            else:
                result[resultPointer] = nums[secondPointer] * nums[secondPointer]
                secondPointer -= 1
            resultPointer -= 1
        return result


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().sortedSquares(nums))
