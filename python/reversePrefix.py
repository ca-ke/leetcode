import sys


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        hasLetter = False
        for char in word:
            stack.append(char)
            if char == ch:
                hasLetter = True
                break

        if hasLetter:
            reversedPrefix = "".join([stack.pop() for _ in range(len(stack))])
            return reversedPrefix + word[len(reversedPrefix) :]
        else:
            return word


print(Solution().reversePrefix(sys.argv[1], sys.argv[2]))
