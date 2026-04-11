class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        c_sum = 0
        for i in range(len(nums)):
            if c_sum < 0:
                c_sum = 0
            c_sum += nums[i]
            res = max(res, c_sum)
        return res
        
        