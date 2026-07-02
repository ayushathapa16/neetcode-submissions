class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for ch in t:
            if ch in count:
                count[ch] -= 1
                if count[ch] == 0:
                    count.pop(ch)
            else:
                return False
        
        if len(count) != 0:
            return False
        return True


        
        