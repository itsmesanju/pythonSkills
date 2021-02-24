import re
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]', '', s).upper()
        """
        :type s: str
        :rtype: bool
        """
        '''
        Idea : use to pointer, one from the begning other from the end (while loop)
                - check if the letter is valid alphanumeric character 
                     - if not move to the next one using while loop 
                - once you get valid letter from both end, compare them 
                    - if they are not equal 
                        - return False
                    - if coninue 
                - if the loop end before return Flase
                    - the string is then palindrom 
                        - So return True 
        '''
        if not s:
            return True
        i = 0
        j = len(s)-1
        print(s)
        while i <=len(s)-1 and j>=0 and i < j:
            # check if the letter is valid alphanumeric character
            while i < len(s)-1 and i < j: 
                i += 1
            #  check if the letter is valid alphanumeric character
            while j > 0 and j > i:
                j-=1
            # Check if they are not equal 
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        return True
