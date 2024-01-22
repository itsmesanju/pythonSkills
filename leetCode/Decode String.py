"""The decodeString algorithm decodes an encoded string that follows a specific pattern. 

It uses a stack to keep track of characters and performs decoding when encountering square brackets. 
The algorithm efficiently handles the repetition of substrings within brackets and constructs the final decoded string by using a stack to maintain the order of characters.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                tempStr= ''

                # pop until s[i] is [
                while stack[-1] != '[':
                    tempStr =  stack.pop()+ tempStr
                
                # remove [
                stack.pop()

                # find repeatedNumber
                repeatedNumber=''
                while stack and stack[-1].isdigit():
                    repeatedNumber =  stack.pop()+ repeatedNumber
                stack.append(tempStr * int(repeatedNumber))
                
            else:
                stack.append(c)
        
        return ''.join(stack)

        
