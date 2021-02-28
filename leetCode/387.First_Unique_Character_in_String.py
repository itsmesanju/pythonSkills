class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
    # Space complexity: Its O(n) cause in the worst case when all chars are unique, the counter will store information of all elements.
    # Time : O(n)
    
class Solution(object):
def firstUniqChar(self, s):
for i,j in enumerate(s):
if(s.count(j)==1):
return i
return -1

# Space O(1)
# Time O(n)
