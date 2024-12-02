import sys
from typing import Counter, List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = Counter(arr)
        counts = list(occurrences.values())
        return len(counts) == len(set(counts))


arr = list(map(int, sys.argv[1].split(",")))
print(Solution().uniqueOccurrences(arr))
