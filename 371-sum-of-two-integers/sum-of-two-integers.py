class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0xFFFFFFFF
        # If the result is negative, get the two's complement positive equivalent
        MASK = 0x80000000

        while b != 0:
            # Carry now contains common set bits of a and b
            carry = a & b

            # Sum of bits of a and b where at least one of the bits is not set
            a = (a ^ b) & MAX

            # Carry is shifted by one so that adding it to a gives the required sum
            b = (carry << 1) & MAX

        # If a is negative, return the negative equivalent in 32 bits representation
        return a if a < MASK else ~(a ^ MAX)