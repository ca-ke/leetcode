import sys


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        targetIndex, startIndex = 0, 0
        if start.replace("_", "") != target.replace("_", ""):
            return False

        startLen = len(start)
        while startIndex < startLen and targetIndex < startLen:
            while startIndex < startLen and start[startIndex] == "_":
                startIndex += 1
            while targetIndex < startLen and target[targetIndex] == "_":
                targetIndex += 1

            if startIndex == startLen or targetIndex == startLen:
                break
            if start[startIndex] == "L" and startIndex < targetIndex:
                return False
            if start[startIndex] == "R" and startIndex > targetIndex:
                return False

            startIndex += 1
            targetIndex += 1

        while startIndex < startLen:
            if start[startIndex] != "_":
                return False
            startIndex += 1

        while targetIndex < startLen:
            if target[targetIndex] != "_":
                return False
            targetIndex += 1

        return True


print(Solution().canChange(sys.argv[1], sys.argv[2]))
