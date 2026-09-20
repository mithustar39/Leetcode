class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in passed:
                return [i,passed[other]]
            passed[nums[i]] = i


        
