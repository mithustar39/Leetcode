class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters = {}
        for c in s:
            characters[c] = characters.get(c,0) + 1
        for i, c in enumerate(s):
            if characters[c] == 1:
                return i
        return -1
