class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=0
        for i in ransomNote:
            if i in magazine:
                c+=1
                magazine=magazine.replace(i,'',1)
        return c==len(ransomNote) 
