from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averageSet = set()

        minPointer, maxPointer = 0, len(nums) - 1

        while minPointer < maxPointer:
            minValue = nums[minPointer]
            maxValue = nums[maxPointer]
            average = (minValue + maxValue) / 2
            averageSet.add(average)
            minPointer += 1
            maxPointer -= 1
        return len(averageSet)
