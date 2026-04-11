class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height, width = len(matrix), len(matrix[0])

        def nullify(ty, tx):
            for y in range(height):
                matrix[y][tx] = None if matrix[y][tx] != 0 else 0
            for x in range(width):
                matrix[ty][x] =  None if matrix[ty][x] != 0 else 0

        for y in range(height):
            for x in range(width):
                if matrix[y][x] == 0:
                    nullify(y, x)
        
        for y in range(height):
            for x in range(width):
                if matrix[y][x] == None:
                    matrix[y][x] = 0
