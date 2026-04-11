class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        for i in range(len(nums)):
            c_sum = 0
            for j in range(i, len(nums)):
                c_sum += nums[j]
                res = max(res, c_sum)
        return res