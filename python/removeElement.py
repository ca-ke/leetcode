import sys
from typing import List


class Solution:
    def remove(self, nums: List[int], position: int):
        for i in range(position + 1, len(nums)):
            nums[i - 1] = nums[i]
        nums[-1] = -1

    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        firstPointer = 0

        while firstPointer < len(nums):
            if nums[firstPointer] == val:
                self.remove(nums, firstPointer)
            else:
                if nums[firstPointer] != -1:
                    result += 1
                firstPointer += 1

        return result


nums = list(map(int, sys.argv[1].split(",")))
value = int(sys.argv[2])
print(Solution().removeElement(nums, value))
