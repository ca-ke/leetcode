import sys


class Solution:
    def isHappy(self, n: int):
        target = n
        seenValues = {}
        while True:
            count = 0
            strn = str(n)
            firstPointer, secondPointer = 0, len(strn) - 1
            while firstPointer <= secondPointer:
                if firstPointer == secondPointer:
                    count += int(strn[firstPointer]) * int(strn[firstPointer])
                else:
                    count += int(strn[firstPointer]) * int(strn[firstPointer]) + int(
                        strn[secondPointer]
                    ) * int(strn[secondPointer])
                n = count
                firstPointer += 1
                secondPointer -= 1

            if seenValues.get(count) is not None:
                seenValues[count] += 1
            else:
                seenValues[count] = 1

            if count == 1:
                return True
            elif count == target or count == 0 or seenValues.get(count) != 1:
                return False


print(Solution().isHappy(int(sys.argv[1])))
