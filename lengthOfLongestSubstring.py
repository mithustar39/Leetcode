class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        maxlen = 0

        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[i])

            maxlen = max(maxlen, i - left + 1)

        return maxlen    

        
