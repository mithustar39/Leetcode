class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for c in s:
            seen[c] = seen.get(c, 0)+1
        seent = {}
        for c in t:
            seent[c] = seent.get(c, 0)+1
        if seen == seent:
            return True
        return False
