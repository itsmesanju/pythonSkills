#Brute force method
# Timee Complexity: O(2n): two loops for each array
# Space Complexity: O(2n): two new arrays

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.makeFinalArray(S) == self.makeFinalArray(T)

    def makeFinalArray(self,arr):
        output=[]
        for item in arr:
            if item != "#":
                output.append(item)
            else:
                if len(output) > 0: 
                   output.pop()
        return str(output)
#
