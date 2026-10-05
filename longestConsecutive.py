class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        maxlength = 0
        
        for num in values:
            if num-1 in values:
                continue
            
            curr = 1

            while (num+1) in values:
                curr+=1
                num+=1
            
            maxlength = max(maxlength, curr)
        
        return maxlength
            
