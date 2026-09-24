from collections import defaultdict

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height, width = len(heights), len(heights[0])
        if height == 1 and width == 1:
            return 0
        target_y, target_x = height-1, width-1
        queue = deque([((0, 0), 0)])  # (cy, cx), c_effort

        visited = {}
        visited[(0, 0)] = 0
        for y in range(height):
            for x in range(width):
                visited[(y, x)] = float('inf')

        while queue:
            (cy, cx), c_effort = queue.pop()

            for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ny, nx = cy+dy, cx+dx
                if 0 <= ny < height and 0 <= nx < width: # inbounds
                    h_diff = abs(heights[cy][cx] - heights[ny][nx])
                    n_effort = max(c_effort, h_diff)
                    if n_effort < visited[(ny, nx)]:
                        visited[(ny, nx)] = n_effort
                        queue.appendleft(((ny, nx), n_effort))
        return visited[(height-1, width-1)]
            
        
