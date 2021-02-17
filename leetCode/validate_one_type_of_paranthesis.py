class Solution:
    def isValid(self, s: str) -> bool:
        count=0
        for char in s:
            if count >= 0:
                if char == '(':
                    count += 1
                if char == ')':
                    count -= 1
            else:
                return False
        
        if count == 0:
            return True
        else:
            return False
