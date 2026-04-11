from copy import deepcopy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def dfs(y, blocked_cols, blocked_diags):
            if y == n:
                board = [["." for _ in range(n)] for _ in range(n)]
                for x, y in blocked_cols.items():
                    board[y][x] = "Q"
                res.append([''.join(row) for row in board])
                return

            for x in range(n):
                diag1 = y+x
                diag2 = "B"+str(y-x)
                if x not in blocked_cols and diag1 not in blocked_diags and diag2 not in blocked_diags:
                    blocked_diags.add(diag1)
                    blocked_diags.add(diag2)
                    blocked_cols[x] = y
                    dfs(y+1, blocked_cols, blocked_diags)
                    del blocked_cols[x]
                    blocked_diags.remove(diag1)
                    blocked_diags.remove(diag2)
        
        dfs(0, {}, set())
        return res


        
