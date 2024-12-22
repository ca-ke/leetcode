import sys


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []

        for element in s:
            if element == "(":
                if stack:
                    result.append(element)
                stack.append(element)
            elif element == ")":
                stack.pop()
                if stack:
                    result.append(element)
        return "".join(result)


print(Solution().removeOuterParentheses(sys.argv[1]))
