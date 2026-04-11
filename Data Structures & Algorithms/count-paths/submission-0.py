from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        queue = deque()
        queue.append((m-1, n-1))

        while queue:
            current = queue.popleft()
            cy, cx = current
            
            for dy, dx in [(0, -1), (-1, 0)]: #[(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = cy+dy, cx+dx
                if 0 <= ny < m and 0 <= nx < n:
                    if dp[ny][nx] == 0:
                        queue.append((ny, nx))
                    dp[ny][nx] += dp[cy][cx]
        
        for row in dp:
            print(row)
        return dp[0][0]
                    
# Thinking:
# Not sure exactly why the paths aren't longer, but i guess they have to somewhat short?