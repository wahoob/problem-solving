class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix = {0 : 1}
        
        for n in nums:
            cur_sum +=  n
            diff = cur_sum - k

            res += prefix.get(diff, 0)
            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1

        return res

