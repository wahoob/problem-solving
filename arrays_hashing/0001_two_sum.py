class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in lookup:
                return i, lookup[remaining]
            lookup[n] = i