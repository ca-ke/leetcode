from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parityArray = [1 if num % 2 != 0 else 0 for num in nums]
        badParity = []
        result = []
        for i in range(1, len(parityArray)):
            if parityArray[i] == parityArray[i - 1]:
                badParity.append(1)
            else:
                badParity.append(0)

        for querie in queries:
            if sum(badParity[querie[0] : querie[1]]) == 1:
                result.append(False)
            else:
                result.append(True)
        return result


print(Solution().isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))
