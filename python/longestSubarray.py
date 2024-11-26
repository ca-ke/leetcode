import sys
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        countZero, lenght, firstPointer, secondPointer = (
            0,
            0,
            0,
            0,
        )

        maxLenght = lenght

        while secondPointer < len(nums):
            if nums[secondPointer] == 0:
                countZero += 1

            while countZero > 1:
                if nums[firstPointer] == 0:
                    countZero -= 1
                firstPointer += 1

            maxLenght = max(maxLenght, secondPointer - firstPointer)
            secondPointer += 1
        return maxLenght


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
print(Solution().longestSubarray(nums))
