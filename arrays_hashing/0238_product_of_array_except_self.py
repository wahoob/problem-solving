class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre, post = 1, 1
        result = []
        for n in nums:
            result.append(pre)
            pre *= n
        
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result