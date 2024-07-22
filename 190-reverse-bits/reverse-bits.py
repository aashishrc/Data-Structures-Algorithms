class Solution:
    def reverseBits(self, n: int) -> int:
        bi = bin(n)[2:]
        bi = bi[::-1]
        if len(bi) < 32:
            bi += "0"*(32 - len(bi))
        return int(bi,2)
        