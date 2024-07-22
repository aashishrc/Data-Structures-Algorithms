class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0xFFFFFFFF
        # # If the result is negative, get the two's complement positive equivalent
        # MASK = 0x80000000

        while (b & MAX) > 0:
            # Carry now contains common set bits of a and b
            carry = (a & b) <<1  

            # Sum of bits of a and b where at least one of the bits is not set
            a = (a ^ b)

            # Carry is shifted by one so that adding it to a gives the required sum
            b = carry
        # If a is negative, return the negative equivalent in 32 bits representation
        return (a & MAX) if b > 0 else a