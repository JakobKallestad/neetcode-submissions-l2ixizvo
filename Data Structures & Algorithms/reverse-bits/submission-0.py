class Solution:
    def reverseBits(self, n: int) -> int:
        b = str(bin(n)[2:]).zfill(32)[::-1]
        return int(b, 2)