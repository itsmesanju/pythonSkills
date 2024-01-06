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

#Dynamic programming.... 
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        result = 0

        for i in range(len(s)):

            #for odd ranges
            left_ptr, right_ptr = i, i

            while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
                result += 1
                left_ptr = left_ptr -1
                right_ptr = right_ptr + 1

            left_ptr, right_ptr = i, i+1
            while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
                result += 1
                left_ptr = left_ptr -1
                right_ptr = right_ptr + 1

        return result


