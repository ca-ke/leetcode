import sys
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setOfNums1 = set(nums1)
        setOfNums2 = set(nums2)

        return [list(setOfNums1 - setOfNums2), list(setOfNums2 - setOfNums1)]


nums1 = list(map(int, sys.argv[1].split(",")))
nums2 = list(map(int, sys.argv[2].split(",")))
print(Solution().findDifference(nums1, nums2))
