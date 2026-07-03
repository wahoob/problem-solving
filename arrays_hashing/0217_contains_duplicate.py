class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicates = {}
        for n in nums:
            if duplicates.get(n, 0) > 0:
                return True
            duplicates[n] = duplicates.get(n, 0) + 1
        return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)