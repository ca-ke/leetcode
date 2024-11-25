import sys
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstPointer, secondPointer, length = 0, 0, len(nums)
        while firstPointer < length - 1:
            if nums[firstPointer] == 0:
                while secondPointer < length:
                    if nums[secondPointer] != 0:
                        nums[firstPointer] = nums[secondPointer]
                        nums[secondPointer] = 0
                        break
                    secondPointer += 1
            firstPointer += 1
            secondPointer = firstPointer + 1


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
Solution().moveZeroes(nums=nums)
