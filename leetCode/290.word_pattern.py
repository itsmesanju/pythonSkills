#Since index() method returns the position at the first occurrence of the specified character, we use it to construct an array of indices.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = []
        map2 = []


        for char in pattern:
            map1.append(pattern.index(char))

        for word in s.split():
            map2.append(s.split().index(word))

        print(map1, map2)
        if map1 == map2:
            return True
        else:
            return False
