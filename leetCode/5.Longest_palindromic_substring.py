def longestPalindrome(s):
    if s == "" or s == len(s) * s[0]:
        return s

    #if all unique character, return first char as palindromic and size 1
    p = s[0]
    l = 1


    for i in range(len(s)):
          for j in range(len(s), 0, -1):
               w = s[i:j]

               # Is 'w' longer than our current longest palindrome 'p'?
               if w == w[::-1] and len(w) > l:
                    p = w
                    l = len(w)
    return p
    #Time O(N^2)
    #Space O(N)
