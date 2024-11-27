import sys
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = -1
        totalSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            leftSum += 0 if i == 0 else nums[i - 1]
            rightSum = totalSum - nums[i] - leftSum
            if rightSum == leftSum:
                return i
        return result


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().pivotIndex(nums))
