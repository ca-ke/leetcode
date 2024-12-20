import sys


class Solution:
    def decodeString(self, s: str) -> str:
        stack = list(reversed(s))
        result = []
        while stack:
            value = stack.pop()
            if value.isnumeric():
                counter = int(value)
                stack.pop()
                target = stack.pop()
                while counter > 0:
                    result.append(target)
                    counter -= 1
                stack.pop()
        return "".join(result)


print(Solution().decodeString(sys.argv[1]))
