#Brute force method to Create list of possible strings and verify if they are palindrome.
class Solution:
    def countSubstrings(self, s: str) -> int:
            def is_pal(string):
                    return string == string[::-1]
                
            substrings = []
            for i in range(len(s)):
                for j in range(i+1, len(s)+1):
                    substrings.append(s[i:j])
            ans = 0

            for s in substrings:
                if is_pal(s):
                    ans += 1
            return ans


