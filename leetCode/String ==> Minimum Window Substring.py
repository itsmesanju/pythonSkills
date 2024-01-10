"""Create a Frequency Map: Generate a frequency map for the characters in the target string (the substring you're looking for).

Sliding Window:
  Initialize two pointers, left and right, to define a window and Move the right pointer to expand the window until you include all characters from the target string.
  
Update Minimum Window: If the current window contains all characters, update the minimum window size.
  Move the left pointer to shrink the window while maintaining the inclusion of all required characters.

Repeat:  Repeat steps 2-3 until the right pointer reaches the end of the string.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Step 1: Create a frequency map for characters in target string
        target_freq = {}
        for char in t:
            target_freq[char] = target_freq.get(char, 0) + 1

        # Step 2-4: Sliding Window
        left, right = 0, 0
        min_len = float('inf')
        min_window_start = 0
        required_chars = len(target_freq)

        while right < len(s):
            # Expand the window
            if s[right] in target_freq:
                target_freq[s[right]] -= 1
                if target_freq[s[right]] == 0:
                    required_chars -= 1

            # Check if the current window contains all required characters
            while required_chars == 0:
                # Update minimum window
                if right - left < min_len:
                    min_len = right - left
                    min_window_start = left

                # Shrink the window
                if s[left] in target_freq:
                    target_freq[s[left]] += 1
                    if target_freq[s[left]] > 0:
                        required_chars += 1

                left += 1

            right += 1

        # Step 5: Return the minimum window substring
        return "" if min_len == float('inf') else s[min_window_start:min_window_start + min_len + 1]
