class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1

        for y in range(m-1, -1, -1):
            for x in range(n-1, -1, -1):
                if y == m-1 and x == n-1:
                    continue
                below = dp[y+1][x] if y+1 < m else 0
                right = dp[y][x+1] if x+1 < n else 0
                dp[y][x] = below + right
        
        return dp[0][0]
