class Solution:
    def addBinary(self, a: str, b: str) -> str:

        """
        We can implement the binary string addition using a simple algorithm, similar to how you would add numbers manually. 
        Start from the rightmost digit and move towards the left, keeping track of the carry. 

        This function iterates through both binary strings, starting from the rightmost digits, 
        adding them along with any carry from the previous step. The result is built from right to left, 
        and the final string represents the sum of the two binary numbers.
        """

        result = ""
        carry = 0

        # Start from the rightmost digits
        i, j = len(a) - 1, len(b) - 1

        # Iterate until we reach the leftmost digits of both strings
        while i >= 0 or j >= 0 or carry:
            # Extract the digits at the current positions (or 0 if out of bounds)
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum and carry
            current_sum = digit_a + digit_b + carry
            carry = current_sum // 2
            current_sum %= 2

            # Add the current result to the left side
            result = str(current_sum) + result

            # Move one position to the left
            i -= 1
            j -= 1

        return result
