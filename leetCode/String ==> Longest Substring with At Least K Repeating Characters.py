class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """if len(s) < k:
            return 0
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)

        return len(s)
        """
        ans = 0

        for uniqueChar in range(1, len(set(s)) + 1):
            d = defaultdict(int)

            l = 0
            for r, char in enumerate(s):
                d[s[r]] += 1

                while len(d) > uniqueChar:
                    d[s[l]] -= 1
                    if d[s[l]] == 0:
                        del d[s[l]]
                    
                    l += 1
                
                if all(val >= k for val in d.values()):
                    ans = max(ans, r - l + 1)

        return ans
