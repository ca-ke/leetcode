import sys
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        writerPointer = 0
        for readerPointer in range(len(nums)):
            if nums[readerPointer] % 2 == 0:
                nums[writerPointer], nums[readerPointer] = (
                    nums[readerPointer],
                    nums[writerPointer],
                )
                writerPointer += 1
        return nums


nums = list(map(int, sys.argv[1].split(",")))
print(Solution().sortArrayByParity(nums))
