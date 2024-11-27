import sys
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = set()

        firstPointer, secondPointer = 0, 0

        while firstPointer < len(nums1) and secondPointer < len(nums2):
            if nums1[firstPointer] < nums2[secondPointer]:
                firstPointer += 1
            elif nums1[firstPointer] > nums2[secondPointer]:
                secondPointer += 1
            else:
                result.add(nums1[firstPointer])
                firstPointer += 1
                secondPointer += 1

        return [value for value in result]


nums1 = list(map(int, sys.argv[1].split(",")))
nums2 = list(map(int, sys.argv[2].split(",")))

print(Solution().intersection(nums1, nums2))
