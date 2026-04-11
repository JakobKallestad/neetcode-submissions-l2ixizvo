from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        height, width = len(grid), len(grid[0])
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    queue.append(((y, x), 0))
                if grid[y][x] == -1:
                    visited.add((y, x))
        
        while queue:
            (cy, cx), c_depth = queue.popleft()

            if (
                (cy, cx) in visited
                or not (0 <= cy < height and 0 <= cx < width)
            ):
                continue
            visited.add((cy, cx))
            
            grid[cy][cx] = min(grid[cy][cx], c_depth)

            queue.append(((cy, cx+1), c_depth+1))
            queue.append(((cy+1, cx), c_depth+1))
            queue.append(((cy, cx-1), c_depth+1))
            queue.append(((cy-1, cx), c_depth+1))


# easy solution is to run BFS from EACH 0 and then keep the minimal value 
# of the one that was there before or the depth from start
# However this could be quite slow in the worst case.
#
# Maybe i could start the search from all the zeros at the same time?
# and then just keep a SHARED visited set.
# and then when all squares have been visited then we know that the depth
# that was when this square was reached should be optimal because BFS makes
# it so that this must have been from the closest 0