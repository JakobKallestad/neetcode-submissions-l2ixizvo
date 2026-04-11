class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for y in range(m-1, -1, -1):
            for x in range(n-2, -1, -1):
                below = dp[y+1][x] if y+1 < m else 0
                right = dp[y][x+1] if x+1 < n else 0
                dp[y][x] = below + right
        
        return dp[0][0]
