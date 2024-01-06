class Solution:
    def longestPalindrome(self, s: str) -> str:
        # One way to solve this could be to check each substring but it will be worst time complexity
        #Instead of bruteforce method, we can traverse the list and assume it as center of the palindrome
        #and try to check on both sides if this is the longest palindrome
            
        result = ""
        resultLength = 0

        for index in range(len(s)):

        #Now, there are two possibilities... what is the string is odd of even characters. Odd can workout assuming one center
        #So, in some cases, we can assume an additional range... to run the function

            #Same code base to handle the off length string
            left_ptr, right_ptr = index, index
            while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
                if (right_ptr - left_ptr + 1) > resultLength:
                    result = s[left_ptr:right_ptr+1]
                    resultLength = right_ptr - left_ptr + 1

                left_ptr = left_ptr - 1
                right_ptr = right_ptr + 1
            
            #Same code base to handle the even length string
            left_ptr, right_ptr = index, index+1
            while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
                if (right_ptr - left_ptr + 1) > resultLength:
                    result = s[left_ptr:right_ptr+1]
                    resultLength = right_ptr - left_ptr + 1

                left_ptr = left_ptr - 1
                right_ptr = right_ptr + 1
        return result
