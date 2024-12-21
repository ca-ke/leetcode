from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        firstPointer, secondPointer = 0, 0
        minValue = 0
        while firstPointer < len(nums1) and secondPointer < len(nums2):
            if nums1[firstPointer] < nums2[secondPointer]:
                firstPointer += 1
            elif nums1[firstPointer] == nums2[secondPointer]:
                minValue = nums1[firstPointer]
                break
            else:
                secondPointer += 1
        return minValue
