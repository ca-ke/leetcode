import sys
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        firstPointer, secondPointer = m - 1, 0
        while firstPointer < len(nums1) and secondPointer < len(nums2):
            num = nums1[firstPointer]
            if num == 0:
                nums1[firstPointer] = nums2[secondPointer]
                secondPointer += 1
            firstPointer += 1

        nums1.sort()


nums1 = list(map(lambda x: int(x), sys.argv[1].split(",")))
m = int(sys.argv[2])
nums2 = list(map(lambda x: int(x), sys.argv[3].split(",")))
n = int(sys.argv[4])

print(Solution().merge(nums1, m, nums2, n))
print(nums1)
