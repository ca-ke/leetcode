import sys


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}

        for letter in magazine:
            if counter.get(letter) is not None:
                counter[letter] += 1
            else:
                counter[letter] = 1

        for letter in ransomNote:
            if counter.get(letter) is None or counter.get(letter) == -1:
                return False
            else:
                counter[letter] -= 1

        return -1 not in counter.values()


ransomNote = sys.argv[1]
magazine = sys.argv[2]
print(Solution().canConstruct(ransomNote, magazine))
