import sys
from typing import List


class Solution:
    def generateSubsets(
        self,
        s: str,
        res: List[List[str]],
        subset: List[str],
        index: int,
    ):
        res.append(subset[:])
        for i in range(index, len(s)):
            subset.append(s[i])
            self.generateSubsets(s, res, subset, i + 1)
            subset.pop()

    def maximumLength(self, s: str) -> int:
        res = []
        subset = []
        self.generateSubsets(s, res, subset, 0)
        print(res)
        return 1


print(Solution().maximumLength(sys.argv[1]))
