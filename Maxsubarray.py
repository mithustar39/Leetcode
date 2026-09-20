class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current = 0
        
        for num in nums:
            current = max(num, current + num)
            max_sum = max(current, max_sum)
        
        return max_sum
