class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag_sum = set()   # r + c
        diag_diff = set()  # r - c

        def dfs(r: int):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                d1 = r + c
                d2 = r - c
                if c in cols or d1 in diag_sum or d2 in diag_diff:
                    continue

                # place
                board[r][c] = "Q"
                cols.add(c); diag_sum.add(d1); diag_diff.add(d2)

                dfs(r + 1)

                # unplace
                board[r][c] = "."
                cols.remove(c); diag_sum.remove(d1); diag_diff.remove(d2)

        dfs(0)
        return res
