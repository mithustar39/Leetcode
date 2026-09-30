class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        

        buckets = [[] for _ in range(len(nums)+1)]

        for key, value in freq.items():
            buckets[value].append(key)
        
        results = []
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                if len(results) == k:
                    return results
                results.append(num)
        return results
