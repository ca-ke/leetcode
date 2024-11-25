import sys
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i, num in enumerate(nums):
            firstPointer, secondPointer = i + 1, len(nums) - 1
            while firstPointer < secondPointer:
                if num + nums[firstPointer] + nums[secondPointer] == 0:
                    result.add((num, nums[firstPointer], nums[secondPointer]))
                    firstPointer += 1
                    secondPointer -= 1
                elif num + nums[firstPointer] + nums[secondPointer] > 0:
                    secondPointer -= 1
                else:
                    firstPointer += 1
        return [list(triplet) for triplet in result]


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
print(Solution().threeSum(nums))
