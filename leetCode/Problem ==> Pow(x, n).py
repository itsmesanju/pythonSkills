class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Check if the exponent n is negative. If so, calculate the reciprocal of x and make n positive.
Initialize a variable result to 1.
Iterate through the bits of the exponent n:
If the current bit is set (i.e., the exponent is odd), multiply result by x.
Square x.
Halve n by shifting its bits to the right.
Return the final value of result, which represents x raised to the power n.
        """
        result = 1
        if n < 0:
            x = 1 / x
            n = -n
        while n:
            if n & 1:  # If n is odd
                result *= x
            x *= x
            n >>= 1  # Bitwise right shift is equivalent to n //= 2
        return result
