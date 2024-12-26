import sys


class Solution:
    def reverseBits(self, n: int) -> int:
        reversedValue = f"{n:032b}"[::-1]
        return int(reversedValue, 2)


print(Solution().reverseBits(int(sys.argv[1])))
