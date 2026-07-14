class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        result = ""
        for c in sorted(count, key=count.get, reverse=True):
            result += c * count[c]

        return result
    
class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in count.items():
            buckets[freq].append(char)

        result = ""
        for freq in range(len(buckets) - 1, 0, -1):
            for char in buckets[freq]:
                result += char * freq
        return result
        
        