class Solution(object):\
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack =[]
        for i in S:
            if i=="(":
                stack.append(i)

            else:
                if i == ")":

                    if stack and stack[-1]=="(": #If stack has data and top element is (. If yes. remove the item as match
                        stack.pop()
                    else:
                        stack.append(i)

        return len(stack)
    

    #without stack
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # _l: number of open parentheses are waiting for close ones
        # _r: number of standalone close parentheses
        _l, _r = 0, 0  
        
        for s in S:
            if(s == '('):
                _l += 1    
            else:
                if _l > 0:
                    _l -= 1
                else:
                    _r +=1
            
        return _l + _r 
