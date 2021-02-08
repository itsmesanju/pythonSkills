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
