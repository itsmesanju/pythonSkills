'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
'''
class Solution:

    def reverse(self, x: int) -> int:
        if str(x).startswith("-"):
                x = str(x)
                x = str(x[1:])
                rev=x[::-1]
                result="-"+rev
        else:
                result=int(str(x)[::-1])
        
        range1= -2**31 
        range2=  2**31
        
        if result in range(range1,range2):
                return result
        else:
                return 0
