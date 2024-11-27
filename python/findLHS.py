import sys
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result, firstPointer, secondPointer = 0, 0, 0
        nums.sort()
        while secondPointer < len(nums):
            secondPointer += 1
            while nums[secondPointer - 1] - nums[firstPointer] > 1:
                firstPointer += 1
            if nums[secondPointer - 1] - nums[firstPointer] == 1:
                result = max(result, secondPointer - firstPointer)

        return result


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().findLHS(nums))
