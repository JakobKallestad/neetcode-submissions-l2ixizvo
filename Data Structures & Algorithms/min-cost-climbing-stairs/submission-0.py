class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 2  # one before and one after
        dp = [float('inf')]*n
        dp[0] = 0
        cost = [0] + cost + [0]
        
        for i in range(n):
            if i < n-1:
                dp[i+1] = min(dp[i+1], dp[i]+cost[i])
            if i < n-2:
                dp[i+2] = min(dp[i+2], dp[i]+cost[i])
        
        return dp[-1]