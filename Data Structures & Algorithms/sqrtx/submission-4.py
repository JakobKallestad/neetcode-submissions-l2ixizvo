class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 0, x
        ans = 0
        while l <= r:
            m = (l+r) // 2
            if x // m >= m:
                l = m + 1
                ans = m
            else:
                r = m - 1
        return ans