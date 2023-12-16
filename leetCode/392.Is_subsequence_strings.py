class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
                if s[i] == t[j]:
                        i += 1
                j += 1

        # i is incrementing only when characters are matching.
        # If i is reached to the end of the string, it means all characters are found
        if i == len(s):
            return True
        else:
            return False
