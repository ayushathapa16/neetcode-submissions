class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        # Hashmap to keep track of characters and their frequency inside the window
        freq = {}
        max_window = 0
        max_freq = 0

        for r in range(0, len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            max_freq = max(max_freq, freq[s[r]])

            # alternate way of doing this:
            # freq[s[r]] = 1 + freq.get(s[r], 0)

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
                max_freq = max(freq.values())
            
            max_window = max(max_window, r - l + 1)
        
        return max_window

        



        