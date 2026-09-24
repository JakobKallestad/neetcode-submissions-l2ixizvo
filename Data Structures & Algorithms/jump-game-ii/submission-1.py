class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*len(nums)
        dp[-1] = 0
        length = len(nums)

        for i in range(length-2, -1, -1):
            e = min(nums[i], length-1-i)
            for j in range(1, e+1):
                dp[i] = min(dp[i+j]+1, dp[i])
        return dp[0]