import sys
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        firstPointer, secondPointer = 0, len(nums) - 1
        leftSum, rightSum = 0, 0
        result = -1
        while firstPointer <= secondPointer:
            if leftSum == rightSum and firstPointer == secondPointer:
                return firstPointer

            if leftSum <= rightSum:
                leftSum += nums[firstPointer]
                firstPointer += 1
            else:
                rightSum += nums[secondPointer]
                secondPointer -= 1

        return result


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().pivotIndex(nums))
