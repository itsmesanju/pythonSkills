class Solution(object):
    def __init__(self):
        self.mem = {}

    def wordBreak(self, s, wordDict):
        # base case, if the whole string is in wordDict
        if s in wordDict:
            return True
        
        # recursive case
        for index in range(1, len(s)):
            # if the substring before index is in wordDict
            if s[:index] in wordDict:
                # get the substring after index
                string = "".join(s[index:])
            
                # check if we have it already
                if string in self.mem:
                    res = self.mem[string]
                    
                    if res == True:
                        return True
                    else:
                        # the substring after index is not in wordDict, and all the combinations of it aren't in wordDict either
                        continue
            
                # we don't have the substring after index in self.mem
                # compute it for the first time
                res = self.wordBreak(string, wordDict)

                # store the result in self.mem
                self.mem[string] = res
                
                if res == True:
                    return True
        
        return False
