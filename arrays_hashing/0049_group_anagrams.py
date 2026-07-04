class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        counts = {}
        for i, s in enumerate(strs):
            val = tuple(sorted(s))
            counts.setdefault(val, []).append(i)

        result = []
        for indices in counts.values():
            group = []
            for i in indices:
                group.append(strs[i])
            result.append(group)
            
        return result
    

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())
    

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1
            groups[tuple(key)].append(s)
        return list(groups.values())