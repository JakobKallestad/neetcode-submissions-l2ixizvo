from collections import deque

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)  # dp[i] = how many subsequences can we make FROM this point onwards
        for i in range(len(dp)-1, -1, -1):
            for j in range(i+1, len(dp)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
