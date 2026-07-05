class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        return list(sorted(counts, key=counts.get ,reverse=True))[:k]
    

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for n in buckets[freq]:
                result.append(n)
                if len(result) == k:
                    return result