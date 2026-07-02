class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the lengths are not equal, then they are not an anagram      
        if len(s) != len(t):
            return False
        
        # build a dictionary with characters of s and their count
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        # compare with t and drecement the counts of characters
        for char in t:
            if char not in counts:
                return False
            counts[char] -= 1
            if counts[char] < 0:
                return False
        
        return True
        






        