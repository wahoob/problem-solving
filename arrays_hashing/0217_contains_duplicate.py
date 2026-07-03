"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least
twice in the array, and false if every element is distinct.

Difficulty: Easy | Topics: Array, Hash Table, Sorting
"""


class Solution:
    """Hash set — early exit on first duplicate.

    Time:  O(n)
    Space: O(n)
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


class SolutionHashMap:
    """Hash map with counts — same idea, heavier structure.

    Time:  O(n)
    Space: O(n)
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicates = {}
        for n in nums:
            if duplicates.get(n, 0) > 0:
                return True
            duplicates[n] = duplicates.get(n, 0) + 1
        return False


class SolutionOneLiner:
    """Length comparison — concise, but always scans the full array.

    Time:  O(n)
    Space: O(n)
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
