from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = defaultdict(int)
        for char in magazine:
            freq[char] = freq[char] + 1
        
        for char in ransomNote:
            if freq[char] == 0:
                return False
            freq[char] -= 1
        
        return True
