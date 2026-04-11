from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        remaining = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 2:
                    queue.append(((y, x), 0))
                elif grid[y][x] == 1:
                    remaining += 1
                elif grid[y][x] == 0:
                    visited.add((y, x))
        
        if remaining == 0:
            return 0

        while queue:
            current, c_depth = queue.popleft()
            cy, cx = current
            
            if (
                current in visited
                or not (0 <= cy < height and 0 <= cx < width)
            ):
                continue
            visited.add(current)
            if grid[cy][cx] == 1:
                remaining -= 1
                if remaining == 0:
                    return c_depth

            queue.append(((cy, cx+1), c_depth+1))
            queue.append(((cy+1, cx), c_depth+1))
            queue.append(((cy, cx-1), c_depth+1))
            queue.append(((cy-1, cx), c_depth+1))
        return -1