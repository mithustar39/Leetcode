class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = 0
        right = n - 1
        output = [1]*n
        
        for i in range(n-1,-1,-1):
            if (nums[left]**2)>(nums[right]**2):
                output[i] = nums[left]**2
                left += 1
            else:
                output[i] = nums[right]**2
                right -= 1
        
        return output
