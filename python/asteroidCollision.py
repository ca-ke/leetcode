import sys
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                print(stack)
                previousAsteroid = stack[-1]
                print(f"{stack} - {previousAsteroid} - {asteroid}")
                while previousAsteroid <= abs(asteroid) and len(stack) > 0:
                    stack.pop()
                    if len(stack) == 0:
                        break
                    previousAsteroid = stack[-1]
            else:
                stack.append(asteroid)
        return stack


asteroids = list(map(int, sys.argv[1].split(",")))
print(Solution().asteroidCollision(asteroids))
