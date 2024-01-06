#Dynamic programming.... 
class Solution:
    def countPalindromeStrings(self, s: str) -> int:
        
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
