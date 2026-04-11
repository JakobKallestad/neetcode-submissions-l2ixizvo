class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums):
            if len(nums) == 1:
                return nums[0]
            # with:
            dp = nums
            dp[1] = max(dp[0], dp[1])
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i-2]+dp[i])
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        return max(house_robber(nums[:-1]), house_robber(nums[1:]))