class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        used = set()
        max_len = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] in used:
                if len(used) > max_len:
                    max_len = len(used)
                while s[r] in used:
                    used.remove(s[l])
                    l += 1
            # applies to both cases       
            used.add(s[r])
            r += 1

        if len(used) > max_len:
            max_len = len(used)
        
        return max_len

                
        



        



        