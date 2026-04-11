class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s_nums = sum(nums)
        if s_nums % 2 != 0:
            return False
        target = s_nums//2
        dp = [False]*(target+1)
        dp[0] = True
        for i in range(len(nums)):  # update DP with ending at index i.
            c = nums[i]
            for j in range(target, -1, -1):
                if dp[j] and j+c <= target:
                    dp[j+c] = True
        return dp[-1]