class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths don't match, then s and t are not anagrams
        if len(s) != len(t):
            return False

        # If the length for both is 1, the letter must be the same
        if len(s) == 1:
            return s == t

        count = {}
        for char in s:
            # If the character already exists in count, then increment its frequency
            if char in count:
                count[char] += 1
            # If the character doesn't exist in count, add to dictionary
            else:
                count[char] = 1
        
        for char in t:
            # If the character doesn't exist in count, return False
            if char not in count:
                return False
            # If character exists in count, decrement its frequency
            count[char] -=1
        
        for element in count:
            # Frequency of a letter in s and t doesn't match
            if count[element] != 0:
                return False
        
        return True
        