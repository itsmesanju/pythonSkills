string="Sanju kumarigtzpqh"
def lengthOfLongestSubstring(s):
        if s is None:
            return 0
        
        
        p1 = 0
        p2 = 0
        
        #'a  b   d   a   b   c   b   b'
        # p1  p2 -> < Sliding Window Algo> 
        
        seen = {}
        maxLen = 0
        while p2 < len(s):
            if seen.get(s[p2]) is None:
                seen[s[p2]]=1
                p2 +=1
                maxLen = max(len(seen),maxLen)  
                # calculate len and compare with maxLen for each unique sub string 
            else:
                seen.pop(s[p1])    # clear the s[p1] from hasmap 
                p1 += 1                 # slide the window i.e. move on p1 to next char
        
        
        
        return maxLen
    
print(lengthOfLongestSubstring(string))
