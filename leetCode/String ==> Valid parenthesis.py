class Solution:
    def isValid(self, s: str) -> bool:
        parantheseMap = {'{':'}', '(':')', '[':']'}
        stack = []
        for character in s:
            if character in parantheseMap:
                stack.append(character)
            elif not stack or character != parantheseMap[stack.pop()]:
                return False
        return not stack
#Add left parentheses to the stack as they are encountered. 
#If we encounter a right parentheses, check if the stack is empty (meaning we didn't previously encounter its match) or if the stack's top element is its pair. 
#At the end return True if the stack is empty


class Solution(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
       return s == ''
