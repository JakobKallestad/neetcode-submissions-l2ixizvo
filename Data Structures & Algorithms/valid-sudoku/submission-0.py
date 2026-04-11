class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = {"1","2","3","4","5","6","7","8","9"} 
        for row in board:
            checked = set()
            for c in row:
                if c != "." and c in valid and c in checked:
                    return False
                checked.add(c)
            #if set(row) != valid:
            #    return False
        
        for x in range(9):
            #col = []
            checked = set()
            for y in range(9):
                c = board[y][x]
                if c != "." and c in valid and c in checked:
                    return False
                checked.add(c)
                #col.append(board[y][x])
            #if set(col) != valid:
            #    return False

        # squares:
        for cy in range(0, 9, 3):
            for cx in range(0, 9, 3):
                checked = set()
                for ay in range(3):
                    for ax in range(3):
                        c = board[cy+ay][cx+ax]
                        if c != "." and c in valid and c in checked:
                            return False
                        checked.add(c)
                #if set(square) != valid:
                #    return False

        return True
                

