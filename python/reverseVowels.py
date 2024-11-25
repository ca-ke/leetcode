import sys


class Solution:
    def isVowel(self, letter: str) -> bool:
        return (
            letter == "a"
            or letter == "A"
            or letter == "e"
            or letter == "E"
            or letter == "i"
            or letter == "I"
            or letter == "o"
            or letter == "O"
            or letter == "u"
            or letter == "U"
        )

    def reverseVowels(self, s: str) -> str:
        result = []
        vowels = []
        for letter in s:
            if self.isVowel(letter):
                vowels.append(letter)

        vowelCount = len(vowels)
        print(vowelCount)
        for i in range(len(s)):
            if self.isVowel(s[i]):
                result.append(vowels[vowelCount - 1])
                vowelCount -= 1
            else:
                result.append(s[i])

        return "".join(result)


print(Solution().reverseVowels(s=sys.argv[1]))
