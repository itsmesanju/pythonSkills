#Using inbuild function of reverse
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char,"").lower()
        rev = ''.join(reversed(s))
        if s.lower() == rev.lower():
            return True
        else:
            return False

#Using two pointers to see if string is palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #First make all strings into lower case and only alphanumeric
        # Initialize 2 pointers. left points to the begining and right points to the end.
        # Next perform two-pointer traversal together and return false if both pointers value is not same.
        
        s = ''.join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

#Using inbuild regular expressions.
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).upper()
        if s == s[::-1]:
            return True
        return False
