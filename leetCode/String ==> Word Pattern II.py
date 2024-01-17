class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
            """
            This approach explores all possible mappings between pattern characters and substrings in s using backtracking. 
            It checks for valid mappings, avoids redundant calculations, and returns True or False based on the existence of a bijective mapping.
            """
            def backtrack(p1, idx, d):
                #p1 (pattern index)
                #idx (string index)
                #d (dictionary for current mappings).

                #If both the pattern index p1 and the string index idx reach the end of their respective strings, 
                #a valid mapping has been found, and the function returns True.

                if p1 == len(pattern) and len(s) == idx:
                    return True

                #If either the string index idx or the pattern index p1 reaches the end of its string, 
                #there is no valid mapping, and the function returns False
                if len(s) == idx or p1 == len(pattern): return False

                #If the current pattern character (pattern[p1]) is already mapped in the dictionary d, 
                #the function checks if the substring in s starting from idx matches the mapped word. If so, it proceeds to the next character; otherwise, it returns False.

                if pattern[p1] in d:
                    if s[idx:].startswith(d[pattern[p1]]):
                        return backtrack(p1+1, idx+len(d[pattern[p1]]), d)
                    else: return False
                
                #If the pattern character is not yet mapped, the function explores all possible substrings starting 
                #from idx and checks if they can be mapped to the current pattern character.

                #The function makes recursive calls with updated indices and mappings after trying each possible mapping.

                for i in range(len(s), idx, -1):
                    t = d.copy()
                    t[pattern[p1]] = s[idx:i]
                    if s[idx:i] in d.values(): return False
                    if backtrack(p1+1, i, t): return True
                return False
            return backtrack(0, 0, {})
