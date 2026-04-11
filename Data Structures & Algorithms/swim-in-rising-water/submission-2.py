from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        queue = deque()
        queue.append(((0, 0), grid[0][0]))
        dist = [[float('inf') for _ in range(width)] for _ in range(height)]

        while queue:
            c_node, c_cost = queue.popleft()
            cy, cx = c_node

            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = cy+dy, cx+dx
                if 0 <= ny < height and 0 <= nx < width:
                    n_cost = max(c_cost, grid[ny][nx])
                    if n_cost < dist[ny][nx]:
                        dist[ny][nx] = n_cost
                        queue.append(((ny, nx), n_cost))
        
        return dist[-1][-1]
            
            


# Reasoning:
# Just Dijkstra?