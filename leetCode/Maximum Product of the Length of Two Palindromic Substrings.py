"""
Initialize arrays left, right, and palindrome_length, all of length n (where n is the length of the input string s).

Use a helper function expand_around_center to find the length of the palindrome centered at a given index. 
Populate the left and right arrays with the start and end indices of palindromes centered at each position.

Calculate the palindrome_length array, representing the length of the palindrome at each index.

Iterate through the string and calculate the maximum product of the lengths of palindromic substrings. This is done by finding the product of the palindrome lengths at each position with the maximum length to the right.

Return the maximum product.

The algorithm uses dynamic programming to efficiently find palindromic substrings and determine their lengths.
"""
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        left, right = [0] * n, [0] * n
        palindrome_length = [0] * n

        # Helper function to find the length of the palindrome centered at the given index
        def expand_around_center(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return (i + 1, j - 1)

        # Populate the left array
        for i in range(n):
            left[i], _ = expand_around_center(i, i)

        # Populate the right array
        for i in range(n - 1, -1, -1):
            _, right[i] = expand_around_center(i, i)

        # Calculate the palindrome_length array
        for i in range(n):
            palindrome_length[i] = right[i] - left[i] + 1

        print(palindrome_length)
        max_product = 0

        for i in range(n - 1):
            max_product = max(max_product, palindrome_length[i] * max(palindrome_length[i + 1:]))

        return max_product

