from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height, width = len(board), len(board[0])
        visited = set()

        for y in range(height):
            for x in range(width):
                if board[y][x] == "X":
                    continue
                escaped = False
                group = set()
                queue = deque()
                queue.append((y, x))
                while queue:
                    current = queue.popleft()
                    cy, cx = current

                    if not (0 <= cy < height and 0 <= cx < width):
                        escaped = True
                        continue
                    if (
                        current in visited
                        or board[cy][cx] == "X"
                    ):
                        continue
                    visited.add(current)
                    group.add(current)
                    
                    queue.append((cy, cx+1))
                    queue.append((cy+1, cx))
                    queue.append((cy, cx-1))
                    queue.append((cy-1, cx))
                
                if not escaped:
                    for sq in group:
                        sqy, sqx = sq
                        board[sqy][sqx] = "X"
                
                    
                    


# rephrase the question from encapsulated 'O's to instead:
# Is there a way to reach outside the board?
# Additionally i need the y and x coordinates of those to change
# I should return to things from my BFS:
# A) did it escape?
# B) all the visited squares so that we can change them if the answer to A) was yes.