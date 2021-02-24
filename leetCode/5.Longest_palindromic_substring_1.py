def longestPalindrome(s):
        s_list = ""
        s_len  = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                rev = s[i:j]
                if s[i:j] == rev[::-1]:
                    if len(rev) > s_len:
                        s_list = s[i:j]
                        s_len = len(rev)
        return s_list
