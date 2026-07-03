class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        anagram = {}
        for l in s:
            anagram[l] = anagram.get(l, 0) + 1

        for l in t:
            if l not in anagram or anagram[l] == 0:
                return False
            anagram[l] = anagram[l] - 1
        
        return True

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)