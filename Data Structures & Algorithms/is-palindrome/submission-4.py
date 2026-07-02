class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = ''
        for char in s:
            if char.isalnum():
                processed_s += char.lower()
        
        return processed_s == processed_s[::-1]


    

        



        