class Solution:
    myCache = {}    # A cache to store the results which are already calculated}
    def climbStairs(self, n: int) -> int:
        
        if n == 0 or n == 1: # if no steps or only 1 step, user will take one step to reach to finish stair
            return 1
        
        if n in self.myCache:    #Check if result is already calculated for the numbera and return the result
            return self.myCache[n]
        
        #If result not available, calculate the result by next below or next-1 stairs. Store the result in cacche.
        res = self.climbStairs(n-1) + self.climbStairs(n-2)  
        self.myCache[n] = res
        return res


    #Time O(n), Space O(n)
