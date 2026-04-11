class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)  # d[i] = how many ways can we make this sum using our coins
        dp[0] = 0
        for i in range(1, amount+1):
            # its basically three ways to reach this new sum from previous sums
            # A) add 1 coin from dp[i-1]
            # B) add 5 coin from dp[i-5]
            # C) add 10 coin from dp[i-10]
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1
        


# Thoughts:
# This seems VERY much like AOC25 problem. Hopefully i can learn something useful here.
