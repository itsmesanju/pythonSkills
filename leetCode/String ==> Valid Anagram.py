class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #        return Counter(s) == Counter(t) #One line solution
        #         return sorted(s) == sorted(t)  #single line solution

        if len(s) != len(t):
            return False
        maps={}
        mapt={}

        for i in s:
            if i not in maps:
                maps[i]=1
            else:
                maps[i] += 1

        for i in t:
            if i not in mapt:
                mapt[i]=1
            else:
                mapt[i] += 1

        if maps == mapt:
            return True
        else:
            return False
