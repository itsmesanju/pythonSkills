class Solution:
    #def isMatch(self, s: str, p: str) -> bool:
    #    return re.match(fr"^{p}$", s) is not None

    def isMatch(self, s: str, p: str) -> bool:
        print("I am here")
        # Create a 2D DP table to store the matching results
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty string and pattern always match
        dp[0][0] = True
        
        # Handle patterns like 'a*', 'b*', 'c*', etc.
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        
        # Iterate through each character in s and each character in p
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # If the characters match or if the pattern has a '.',
                    # the result depends on the previous characters
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # If the current pattern character is '*', 
                    # check if the previous pattern character matches the current string character or '.'
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        # '*' matches zero or more of the preceding element
                        # '*' counts as 0, 1, or multiple preceding character
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]  
                    else:
                        # '*' counts as 0 preceding character
                        dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = False
                    
        return dp[len(s)][len(p)]
