class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while target != (numbers[left]+numbers[right]):
            if numbers[left]+numbers[right] < target:
                left += 1
            if numbers[left]+numbers[right] > target:
                right -= 1
        
        return [left+1, right+1]
