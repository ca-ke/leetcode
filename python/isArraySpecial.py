from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parityArray = [1 if num % 2 != 0 else 0 for num in nums]
        badParity = [
            1 if parityArray[i] == parityArray[i - 1] else 0
            for i in range(1, len(parityArray))
        ]

        prefixSum = [0] * (len(badParity) + 1)
        for i in range(len(badParity)):
            prefixSum[i + 1] = prefixSum[i] + badParity[i]

        result = []
        for query in queries:
            start, end = query
            bad_count = prefixSum[end] - prefixSum[start]
            result.append(bad_count == 0)

        return result


print(Solution().isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))
