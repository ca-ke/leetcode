import sys
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        diffSet = [abs(seats[i] - students[i]) for i in range(0, len(seats))]
        return sum([abs(value) for value in diffSet])


seats = list(map(int, sys.argv[1].split(",")))
students = list(map(int, sys.argv[2].split(",")))
print(Solution().minMovesToSeat(seats, students))
