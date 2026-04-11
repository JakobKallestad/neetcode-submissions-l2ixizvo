from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        stack = deque()

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1 and (y, x) not in visited:
                    # start a new island DFS
                    stack.append((y, x))
                    island_area = 0

                    while stack:
                        cy, cx = stack.pop()
                        if (
                            (cy, cx) in visited
                            or not (0 <= cy < len(grid) and 0 <= cx < len(grid[0]))
                            or grid[cy][cx] != 1
                        ):
                            continue

                        visited.add((cy, cx))
                        island_area += 1

                        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            stack.append((cy + dy, cx + dx))

                    max_area = max(max_area, island_area)

        return max_area
