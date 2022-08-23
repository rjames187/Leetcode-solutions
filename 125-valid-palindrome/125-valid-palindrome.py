class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(filter(lambda char: (char.isalnum()), s))
        
        return s == s[::-1]