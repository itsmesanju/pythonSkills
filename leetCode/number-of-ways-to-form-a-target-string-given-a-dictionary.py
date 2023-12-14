from functools import lru_cache
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        #Create counter of each character vs alphabets
        counter = [[0]*26 for _ in range(len(words[0]))]
        
        for word in words:
            #Creating 2D counters array for each word in words
            #The ord in this code is to convert a character to its Unicode code point.
            # It's being used to map each character to a numeric index in the range [0, 25], corresponding to the English alphabet (assuming lowercase letters).
            # First we generate the unicode of the chatacyer and then subtract the A's value... so it will be turn the index as 0 to 25

            for i in range(len(word)):
                counter[i][ord(word[i])-ord('a')] += 1

        @lru_cache(maxsize=None)  # None means unlimited cache size

        #The num_ways function is a recursive algorithm within the Solution class that calculates the number of ways to form a target string
        # from a given list of words. It iterates through the characters of the target string, considering the count of each character at the 
        # corresponding positions in the words. The function checks whether the target string is fully formed or if the end of the words array has been reached. 
        # Depending on the conditions, it either returns 1, 0, or recursively calculates the number of ways by considering the availability of characters at each position. 
        # The result is the total count of valid combinations, and the modulo operation is applied to avoid integer overflow. 
      
      
        def num_ways(word_idx, target_idx):
            if target_idx == len(target):
                return 1
            elif word_idx == len(counter):
                return 0
            else:
                res = 0
                curr = ord(target[target_idx]) - ord('a')
                if counter[word_idx][curr] > 0:
                    res += counter[word_idx][curr] * num_ways(word_idx+1, target_idx+1)
                res += num_ways(word_idx+1, target_idx)
                return res % (10**9+7)

        return num_ways(0,0)
