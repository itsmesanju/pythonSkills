class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        #To solve this problem, we can use the sliding window technique. 

        from collections import Counter

        result = []
        len_s, len_p = len(s), len(p)
        
        # Counter for pattern string
        p_counter = Counter(p)
        
        # Counter for the first window in s
        s_counter = Counter(s[:len_p])
        
        # Check if the first window is an anagram
        if s_counter == p_counter:
            result.append(0)
        
        # Iterate through the rest of the string
        for i in range(1, len_s - len_p + 1):
            # Update the window's Counter by removing the leftmost character and adding the new character
            s_counter[s[i - 1]] -= 1
            if s_counter[s[i - 1]] == 0:
                del s_counter[s[i - 1]]
            s_counter[s[i + len_p - 1]] += 1
            
            # Check if the current window is an anagram
            if s_counter == p_counter:
                result.append(i)
        
        return result
