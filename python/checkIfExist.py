import sys
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seenElements = set()

        for num in arr:
            if num * 2 in seenElements or (num % 2 == 0 and num // 2 in seenElements):
                return True
            seenElements.add(num)
        return False


arr = list(map(int, sys.argv[1].split(",")))
print(Solution().checkIfExist(arr))
