import sys
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        firstPointer, secondPointer, count, highestCount, highestValue = (
            0,
            1,
            1 / 2,
            0,
            0,
        )
        nums.sort()
        while secondPointer < len(nums):
            if count >= highestCount:
                highestCount = count
                highestValue = nums[firstPointer]

            if nums[firstPointer] == nums[secondPointer]:
                count += 1 / 2
            else:
                count = 1 / 2
            firstPointer += 1
            secondPointer += 1

        return highestValue


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
print(Solution().majorityElement(nums))
