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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        temp = []
        """
        In this implementation, we are navigating all characters in the string and appending them into an empty array. 
        if char is already encountered, we pop the element from the beginning of temp until the list no longer contains the repeating character.

        """
        for char in s:
            while char in temp:
                temp.pop(0)
            temp.append(char)

            result = max(result, len(temp))

        return result
