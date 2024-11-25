import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstValue = float("inf")
        secondValue = float("inf")
        for num in nums:
            if num <= firstValue:
                firstValue = num
            elif num > firstValue and num <= secondValue:
                secondValue = num
            else:
                return True
        return False


nums = list(map(lambda x: int(x), sys.argv[1].split(",")))
print(Solution().increasingTriplet(nums=nums))
