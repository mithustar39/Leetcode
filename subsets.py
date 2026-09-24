class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        current = []
        output = []
        def helper(i):
            if i == len(nums):
                output.append(current.copy())
                return
            
            current.append(nums[i])
            helper(i+1)
            current.pop()

            helper(i+1)
        
        helper(0)
        return output
