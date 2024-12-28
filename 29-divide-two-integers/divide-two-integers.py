class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 0 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1

        divisor = abs(divisor)
        dividend = abs(dividend)

        i = 0
        while dividend >= divisor:
            cnt = 0
            while dividend >= (divisor << (cnt + 1)):
                cnt +=1
            i += (1 << cnt )
            dividend -= (divisor << cnt)
        if i >= (1 << 31) and sign:
            return (1 << 31) - 1
        elif i >= (1 << 31) and not sign:
            return -(1 << 31)
        if sign:
            return i
        return -i

# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1
#         dividend = abs(dividend)
#         divisor = abs(divisor)
#         result = len(range(0, dividend-divisor+1, divisor))
#         if sign == -1:
#             result = -result
#         minus_limit = -(2**31)
#         plus_limit = (2**31 - 1)
#         result = min(max(result, minus_limit), plus_limit)
#         return result