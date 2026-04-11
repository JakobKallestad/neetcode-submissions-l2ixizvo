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
            print(dp)
        return dp[-1]


        





# Thoughts:
# This seems really easy to do:
# Just loop over the breakpoint in O(n) time, and then check the sum(p1)==sum(p2)
# I could speed it up by caching the sums each time and always updating them when i iterate the breakpoint
# If that is all, then this is very easy and in my opinion barely DP as its only used to make it go fast.
# Never mind --> there is no breakpoint. These are subsets. But we might have duplicate numbers.
