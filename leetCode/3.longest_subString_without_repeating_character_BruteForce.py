class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
          String1 = ''
          String2 = ''
          for currentChar in s:
              if currentChar in String1:
                  i = String1.index(currentChar)
                  String1 = String1[i+1:] + currentChar
              else:
                  String1 += currentChar
                  if len(String1) > len(String2):
                      String2 = String1
          return len(String2)
#Time complexity O(n)
#Space complexity O(2n)


