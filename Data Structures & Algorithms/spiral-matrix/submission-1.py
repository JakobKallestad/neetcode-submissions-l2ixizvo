class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height, width = len(matrix), len(matrix[0])
        n_squares = height*width
        ordered_set = dict()
        dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        di = 0
        cy, cx = 0, -1
        while len(ordered_set) < n_squares:
            dy, dx = dir_list[di]
            ny, nx = cy+dy, cx+dx
            if (ny, nx) in ordered_set or not (0 <= ny < height and 0 <= nx < width):
                di = (di+1)%4
            else:
                ordered_set[(ny, nx)] = matrix[ny][nx]
                cy, cx = ny, nx
            print(cy, cx)

        return list(ordered_set.values())
