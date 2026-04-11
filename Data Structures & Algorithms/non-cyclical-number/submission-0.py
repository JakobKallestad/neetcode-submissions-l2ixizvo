class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            digits = list(str(n))
            d_sum_2 = sum([d**2 for d in map(int, digits)])
            if d_sum_2 == 1:
                return True
            if d_sum_2 in visited:
                return False
            visited.add(d_sum_2)
            n = d_sum_2
        